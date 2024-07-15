import datetime
import os.path
import pickle
import sys
import time
import traceback
from pprint import pprint
from typing import List, Dict, AnyStr, Any

import pandas as pd

sys.path.append('..')

from utils.validation import validate_season_string

from nba_api.stats.static.teams import get_teams

from featurevec.feature_vector_helper import get_season_games_for_team, get_referee, \
    aggregate_simple_game_cume_stats, \
    get_longest_lineup, get_offdef_rating, get_player_efficiency, get_date_from_game_id, print_df, \
    get_league_game_log_for_season
from utils.helper_functions import get_home_away_team, get_opponent, add_suffix_to_keys
from utils.constants import LOG_FILE, FV_COLS


def get_starting_dataset(seasons: List[str]):
    """
    Get the roster of all teams for a given season.

    :param seasons: The seasons to get the roster for.
    :return: A dictionary containing the roster of all teams for the given seasons and the games played by the team.
    Example structure
    team_season_by_game = {
        '2019-20': {
            'game_id_1': {
                'team_ticker': 'LAL',
                'opponent': 'LAC',
                'date': '2020-01-01',
                'home': True,
                'playoff': False
            },
        }
    }
    """
    map(validate_season_string, seasons)

    teams = get_teams()

    seasons.sort()
    seasons_suffixes = []
    for i in range(len(seasons)):
        seasons_suffixes.append(seasons[i].split('-')[1])

    team_season_by_game = {}
    # temp_team_season_by_game = {}

    file_name_prefix = '../data/games_by_season_'

    for season, season_suffix in zip(seasons, seasons_suffixes):
        # Load the data if it exists
        if os.path.exists(f'{file_name_prefix}{season_suffix}.pickle'):
            logger.info(f'Loading data for season {season}')
            team_season_by_game[season] = pickle.load(open(f'{file_name_prefix}{season_suffix}.pickle', 'rb'))
            continue

        logger.info(f'Processing season {season}')
        team_season_by_game = {season: {}}
        # Set of game ids of this season
        game_ids = set()
        for team_id, team_ticker in map(lambda x: (x['id'], x['abbreviation']), teams):
            logger.info(f'Processing team {team_id} ({team_ticker})')

            # __________________REGULAR SEASON GAMES__________________
            # Getting season games for team
            reg_season_games_log = get_season_games_for_team(team_ticker, season, playoffs=False)
            df_reg_season_games = pd.DataFrame(reg_season_games_log)
            df_reg_season_games.loc[:, 'game_date'] = pd.to_datetime(df_reg_season_games['game_date'],
                                                                     format='%b %d, %Y')
            df_reg_season_games.sort_values(by='game_date', inplace=True, ascending=True)
            df_reg_season_games.reset_index(drop=True, inplace=True)

            for idx, row in df_reg_season_games.iterrows():
                # Skip if the game id is already in the set
                if row['game_id'] in game_ids:
                    logger.debug(f'Skipping game {row["game_id"]} for team {team_ticker} as it is already processed')
                    continue
                game_ids.add(row['game_id'])

                logger.debug(f'Adding game {row["game_id"]} for team {team_ticker}')
                team_season_by_game[season].update({
                    row['game_id']: {
                        'team_ticker': team_ticker,
                        'opponent': get_opponent(team_ticker, row['matchup']),
                        'date': row['game_date'],
                        'home': get_home_away_team(row['matchup'])['home_team'] == team_ticker,
                        'playoff': False
                    }
                })

            # __________________PLAYOFF GAMES__________________
            # Getting playoff games for team
            playoff_games_log = get_season_games_for_team(team_ticker, season, playoffs=True)
            # Skip if there are no playoff games
            if not playoff_games_log:
                continue

            df_playoff_games = pd.DataFrame(playoff_games_log)
            df_playoff_games.loc[:, 'game_date'] = pd.to_datetime(df_playoff_games['game_date'],
                                                                  format='%b %d, %Y')
            df_playoff_games.sort_values(by='game_date', inplace=True, ascending=True)
            df_playoff_games.reset_index(drop=True, inplace=True)

            for idx, row in df_playoff_games.iterrows():
                # Skip if the game id is already in the set
                if row['game_id'] in game_ids:
                    logger.debug(f'Skipping game {row["game_id"]} for team {team_ticker} as it is already processed')
                    continue
                game_ids.add(row['game_id'])

                logger.debug(f'Adding game {row["game_id"]} for team {team_ticker}')
                team_season_by_game[season].update({
                    row['game_id']: {
                        'team_ticker': team_ticker,
                        'opponent': get_opponent(team_ticker, row['matchup']),
                        'date': row['game_date'],
                        'home': get_home_away_team(row['matchup'])['home_team'] == team_ticker,
                        'playoff': True
                    }
                })

        pickle.dump(team_season_by_game[season], open(f'{file_name_prefix}{season_suffix}.pickle', 'wb'))
        logger.info(f'Data for season {season} saved')

    return team_season_by_game


def get_feature_vector(season: str, team_ticker: str, opp_team_ticker: str, is_team_home: bool,
                       game_id: str, playoffs: bool) -> Dict[AnyStr, Any]:
    """
    Get the feature vector for a game.

    :param season: A string representing the season in the format 'YYYY-YY'.
    :param team_ticker: A string representing the team abbreviation.
    :param opp_team_ticker: A string representing the opponent team abbreviation.
    :param is_team_home: A boolean representing if the team (not opp_team) is the home team.
    :param game_id: A string representing the game id.
    :param playoffs: A boolean representing if the game is a playoff game.
    :return: A dictionary containing the feature vector for the game.
    """

    start_time = time.time()
    simple_season_stats = aggregate_simple_game_cume_stats(team_ticker, season, playoffs, game_id)
    logger.debug(f'Aggregate simple game cume stats took {time.time() - start_time} seconds')

    start_time = time.time()
    # distance_travelled = get_distance_travelled(team_ticker, game_id, season, playoffs)
    longest_lineup = get_longest_lineup(team_ticker, opp_team_ticker, game_id, season, playoffs)
    logger.debug(f'Get longest lineup took {time.time() - start_time} seconds')

    start_time = time.time()
    off_def_rating = get_offdef_rating(team_ticker, season, game_id, playoffs)
    logger.debug(f'Get offdef rating took {time.time() - start_time} seconds')

    start_time = time.time()
    simple_season_stats_opp = aggregate_simple_game_cume_stats(opp_team_ticker, season, playoffs, game_id)
    logger.debug(f'Aggregate simple game cume stats for opponent took {time.time() - start_time} seconds')

    start_time = time.time()
    # distance_travelled_opp = get_distance_travelled(opp_team_ticker, game_id, season, playoffs)
    longest_lineup_opp = get_longest_lineup(opp_team_ticker, team_ticker, game_id, season, playoffs)
    logger.debug(f'Get longest lineup for opponent took {time.time() - start_time} seconds')

    start_time = time.time()
    off_def_rating_opp = get_offdef_rating(opp_team_ticker, season, game_id, playoffs)
    logger.debug(f'Get offdef rating for opponent took {time.time() - start_time} seconds')

    start_time = time.time()
    lineup_efficiency = 0
    for lineup_player in longest_lineup['lineup']:
        lineup_efficiency += get_player_efficiency(lineup_player['id'], team_ticker, game_id, season)
    logger.debug(f'Get player efficiency for lineup took {time.time() - start_time} seconds')
    lineup_efficiency /= len(longest_lineup['lineup'])

    # start_time = time.time()
    # bench_efficiency = 0
    # for bench_player in longest_lineup['bench']:
    #     bench_efficiency += get_player_efficiency(bench_player['id'], team_ticker, game_id, season)
    # logger.debug(f'Get player efficiency for bench took {time.time() - start_time} seconds')
    # bench_efficiency /= len(longest_lineup['bench'])

    start_time = time.time()
    lineup_efficiency_opp = 0
    for lineup_player in longest_lineup_opp['lineup']:
        lineup_efficiency_opp += get_player_efficiency(lineup_player['id'], opp_team_ticker, game_id, season)
    logger.debug(f'Get player efficiency for lineup opponent took {time.time() - start_time} seconds')
    lineup_efficiency_opp /= len(longest_lineup_opp['lineup'])

    # start_time = time.time()
    # bench_efficiency_opp = 0
    # for bench_player in longest_lineup_opp['bench']:
    #     bench_efficiency_opp += get_player_efficiency(bench_player['id'], opp_team_ticker, game_id, season)
    # logger.debug(f'Get player efficiency for bench opponent took {time.time() - start_time} seconds')
    # bench_efficiency_opp /= len(longest_lineup_opp['bench'])

    regseas_gamelog = get_league_game_log_for_season(season, playoffs=False)
    playoff_gamelog = get_league_game_log_for_season(season, playoffs=True)
    regseas_gamelog = pd.DataFrame(regseas_gamelog)
    playoff_gamelog = pd.DataFrame(playoff_gamelog)
    gamelog = pd.concat([regseas_gamelog, playoff_gamelog])
    gamelog.reset_index(drop=True, inplace=True)

    game_team = gamelog.loc[(gamelog['game_id'] == game_id) & (
                gamelog['team_abbreviation'] == team_ticker)]
    game_opponent = gamelog.loc[(gamelog['game_id'] == game_id) & (
                gamelog['team_abbreviation'] == opp_team_ticker)]

    home_team_game = game_team if is_team_home else game_opponent
    away_team_game = game_team if not is_team_home else game_opponent

    misc_stats = {
        'lineup_efficiency': lineup_efficiency,
        # 'bench_efficiency': bench_efficiency,
        # 'distance_travelled': distance_travelled,
    }
    misc_stats_opp = {
        'lineup_efficiency': lineup_efficiency_opp,
        # 'bench_efficiency': bench_efficiency_opp,
        # 'distance_travelled': distance_travelled_opp,
    }
    misc = {
        'home_team': team_ticker if is_team_home else opp_team_ticker,
        'away_team': opp_team_ticker if is_team_home else team_ticker,
        'game_id': game_id,
        'winner': 'home' if home_team_game['pts'].values[0] > away_team_game['pts'].values[0] else 'away',
        'pts_H': home_team_game['pts'].values[0],
        'pts_A': away_team_game['pts'].values[0],
    }

    simple_season_stats.pop('team_id')
    simple_season_stats.pop('season')

    simple_season_stats_opp.pop('team_id')
    simple_season_stats_opp.pop('season')

    if is_team_home:
        off_def_rating = add_suffix_to_keys(off_def_rating, 'H')
        simple_season_stats = add_suffix_to_keys(simple_season_stats, 'H')
        misc_stats = add_suffix_to_keys(misc_stats, 'H')
        off_def_rating_opp = add_suffix_to_keys(off_def_rating_opp, 'A')
        simple_season_stats_opp = add_suffix_to_keys(simple_season_stats_opp, 'A')
        misc_stats_opp = add_suffix_to_keys(misc_stats_opp, 'A')
    else:
        off_def_rating = add_suffix_to_keys(off_def_rating, 'A')
        simple_season_stats = add_suffix_to_keys(simple_season_stats, 'A')
        misc_stats = add_suffix_to_keys(misc_stats, 'A')
        off_def_rating_opp = add_suffix_to_keys(off_def_rating_opp, 'H')
        simple_season_stats_opp = add_suffix_to_keys(simple_season_stats_opp, 'H')
        misc_stats_opp = add_suffix_to_keys(misc_stats_opp, 'H')

    referee = get_referee(game_id)

    return {
        **simple_season_stats,
        **simple_season_stats_opp,
        **off_def_rating,
        **off_def_rating_opp,
        **misc_stats,
        **misc_stats_opp,
        **misc,
        'season': season,
        'date': get_date_from_game_id(game_id),
        'playoff': playoffs,
        'referee_name': referee['name'],
        'referee_id': referee['id']
    }


def is_team_home(team_ticker: str, game_id: str, season: str) -> bool:
    """
    Check if the team is the home team in a game.

    :param team_ticker: A string representing the team abbreviation.
    :param game_id: A string representing the game id.
    :param season: A string representing the season in the format 'YYYY-YY'.
    :return: A boolean representing if the team is the home team.
    """
    team_game_log = get_season_games_for_team(team_ticker, season, False)
    team_game_log.extend(get_season_games_for_team(team_ticker, season, True))
    for game in team_game_log:
        if game['game_id'] == game_id:
            return get_home_away_team(game['matchup'])['home_team'] == team_ticker


def get_game_id_and_season_type(team_ticker: str, season: str, date: str) -> Dict[str, Any]:
    """
    Get the game id of the game for the team.

    :param team_ticker: The team abbreviation.
    :param season: The season in the format 'YYYY-YY'.
    :param date: The date of the game in the format 'YYYY-MM-DD'.
    :return: A dict containing the game id and a boolean representing if the game is a playoff game.
    """
    reg_team_game_log = get_season_games_for_team(team_ticker, season, False)
    po_team_game_log = get_season_games_for_team(team_ticker, season, True)

    date = datetime.datetime.strptime(date, '%Y-%m-%d')

    for game in reg_team_game_log:
        if date == datetime.datetime.strptime(game['game_date'], '%b %d, %Y'):
            return {'game_id': game['game_id'], 'playoff': False}

    for game in po_team_game_log:
        if date == datetime.datetime.strptime(game['game_date'], '%b %d, %Y'):
            return {'game_id': game['game_id'], 'playoff': True}


import logging

# log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] [%(name)s] %(message)s")
# root_logger = logging.getLogger()
#
# fileHandler = logging.FileHandler(f"{LOG_FILE}")
# fileHandler.setFormatter(log_formatter)
# root_logger.addHandler(fileHandler)
#
# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(log_formatter)
# root_logger.addHandler(consoleHandler)
#
# logger = logging.getLogger(os.path.basename(__file__))
# logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    seasons = ['2022-23', '2023-24']
    # seasons = ['2021-22', '2022-23', '2023-24']
    # seasons = ['2020-21', '2021-22', '2022-23', '2023-24']
    # seasons = ['2019-20', '2020-21', '2021-22', '2022-23', '2023-24']

    start_dataset = get_starting_dataset(seasons)

    logger.info("STARTING CALCULATION")
    for season in start_dataset:
        logger.info(f'Calculating f.vecs. for season: {season}')

        game_ids_processed = set()

        # If file exists, load it and skip the games that are already processed
        if os.path.exists(f'../data/feature_vector/fv_{season}.csv'):
            df = pd.read_csv(f'../data/feature_vector/fv_{season}.csv', dtype={
                'game_id': str,
                'home_team': str,
                'away_team': str,
                'season': str,
                'referee_id': int
            })
            game_ids_processed = set(df['game_id'].unique()) if len(df) > 0 else set()
        else:
            df = pd.DataFrame(columns=FV_COLS)
            game_ids_processed = set()
            # Create empty file with the header
            df.to_csv(f'../data/feature_vector/fv_{season}.csv', index=False)

        logger.debug(f'game_ids already process = {len(game_ids_processed)}')

        games = start_dataset[season]
        for game_id in games:
            logger.info(f'Calculating f.vecs. for game: {game_id}')

            game = games[game_id]
            feature_vector = {}

            if game_id in game_ids_processed:
                continue

            feature_vector = {}

            logger.info(f'Calculating f.vecs. for game: {game_id} for season {season}')

            success = False
            while not success:
                try:
                    start_time = time.time()
                    feature_vector = get_feature_vector(season, game['team_ticker'], game['opponent'], game['home'],
                                                        game_id, game['playoff'])

                    pprint(feature_vector)

                    logger.debug(
                        f'Feature vector calculation for game {game_id} took {time.time() - start_time} seconds')

                    dataframe = pd.DataFrame([feature_vector], columns=FV_COLS)
                    dataframe.to_csv(f'../data/feature_vector/fv_{season}.csv', mode='a', index=False,
                                     header=False)
                    logger.debug('Feature vectors saved')
                    success = True
                    game_ids_processed.add(game_id)
                except Exception as e:
                    logger.error(f'Error occured for game {game_id}')
                    logger.error(e)
                    traceback.print_exc()
                    feature_vector = {}
                    success = False
                    time.sleep(1)

            # logger.debug(f'Saving feature vectors for team {team_ticker}, season {season}')
            # with open(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', 'wb') as f:
            #     dataframe = pd.DataFrame(feature_vectors)
            #     dataframe.to_csv(f, index=False, mode='a', header=False)
