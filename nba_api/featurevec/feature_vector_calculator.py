import datetime
import os.path
import pickle
import random
import sys
import time
import traceback
from pprint import pprint
from typing import List, Dict, AnyStr, Any

import pandas as pd

sys.path.append('..')

from utils.validation import validate_season_string

from nba_api.stats.static.teams import get_teams

from feature_vector_helper import get_common_team_roster, get_season_games_for_team, get_referee, \
    aggregate_simple_game_cume_stats, \
    get_longest_lineup, get_offdef_rating, get_player_efficiency, get_date_from_game_id
from utils.helper_functions import get_home_away_team, get_opponent, add_suffix_to_keys
from utils.constants import FV_COLS, LOG_FILE


def get_starting_dataset(seasons: List[str]):
    """
    Get the roster of all teams for a given season.

    :param seasons: The seasons to get the roster for.
    :return: A dictionary containing the roster of all teams for the given seasons and the games played by the team.
    Example structure
    teams_players_by_season = {
        '2019-20': {
            'ATL': {
                'id': 1610612737,
                'players': [11111, 22222]
                'reg_season_games': [
                    {
                        'game_id': '0021900001',
                        'date': '2019-10-24',
                        'home': True,
                        'opponent': 'DET'
                    }
                ],
                'playoff_games': [
                    {
                        'game_id': '0041900401',
                        'date': '2020-08-17',
                        'home': False,
                        'opponent': 'MIL'
                    }
                ]
            }
        }
    }
    """
    map(validate_season_string, seasons)

    teams = get_teams()

    seasons.sort()
    seasons_suffixes = []
    for i in range(len(seasons)):
        seasons_suffixes.append(seasons[i].split('-')[1])

    teams_players_by_season = {}
    temp_teams_players_by_season = {}

    file_name_prefix = '../data/teams_players_games_by_season_'

    for season, season_suffix in zip(seasons, seasons_suffixes):
        if not os.path.exists(f'{file_name_prefix}{season_suffix}.pickle'):
            print(f'Processing season {season}')
            temp_teams_players_by_season = {}
            temp_teams_players_by_season[season] = {}
            for team_id, team_ticker in map(lambda x: (x['id'], x['abbreviation']), teams):
                print(f'Processing team {team_id} ({team_ticker})')
                temp_teams_players_by_season[season].update({team_ticker: {'id': team_id, 'players': []}})
                roster = get_common_team_roster(team_id, season)
                for player in roster:
                    temp_teams_players_by_season[season][team_ticker]['players'].append(player['player_id'])

                temp_teams_players_by_season[season][team_ticker]['reg_season_games'] = []
                reg_season_games_log = get_season_games_for_team(team_ticker, season, playoffs=False)
                df_reg_season_games = pd.DataFrame(reg_season_games_log)
                df_reg_season_games.loc[:, 'game_date'] = pd.to_datetime(df_reg_season_games['game_date'],
                                                                         format='%b %d, %Y')
                df_reg_season_games.sort_values(by='game_date', inplace=True, ascending=True)
                df_reg_season_games.reset_index(drop=True, inplace=True)

                for idx, row in df_reg_season_games.iterrows():
                    temp_teams_players_by_season[season][team_ticker]['reg_season_games'].append({
                        'game_id': row['game_id'],
                        'date': row['game_date'],
                        'home': get_home_away_team(row['matchup'])['home_team'] == team_ticker,
                        'opponent': get_opponent(row['matchup'])
                    })

                temp_teams_players_by_season[season][team_ticker]['playoff_games'] = []
                playoff_games_log = get_season_games_for_team(team_ticker, season, playoffs=True)
                if playoff_games_log:
                    df_playoff_games = pd.DataFrame(playoff_games_log)
                    df_playoff_games.loc[:, 'game_date'] = pd.to_datetime(df_playoff_games['game_date'],
                                                                          format='%b %d, %Y')
                    df_playoff_games.sort_values(by='game_date', inplace=True, ascending=True)
                    df_playoff_games.reset_index(drop=True, inplace=True)

                    for idx, row in df_playoff_games.iterrows():
                        temp_teams_players_by_season[season][team_ticker]['playoff_games'].append({
                            'game_id': row['game_id'],
                            'date': row['game_date'],
                            'home': get_home_away_team(row['matchup'])['home_team'] == team_ticker,
                            'opponent': get_opponent(row['matchup'])
                        })

            pickle.dump(temp_teams_players_by_season, open(f'{file_name_prefix}{season_suffix}.pickle', 'wb'))
        else:
            temp_teams_players_by_season = pickle.load(open(f'{file_name_prefix}{season_suffix}.pickle', 'rb'))

        teams_players_by_season.update(temp_teams_players_by_season)

    return teams_players_by_season


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
        'referee': get_referee(game_id)
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

log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] [%(name)s] %(message)s")
root_logger = logging.getLogger()

fileHandler = logging.FileHandler(f"{LOG_FILE}")
fileHandler.setFormatter(log_formatter)
root_logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(log_formatter)
root_logger.addHandler(consoleHandler)

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    seasons = ['2021-22', '2022-23', '2023-24']

    start_dataset = get_starting_dataset(seasons)

    logger.info("STARTING CALCULATION")
    for season in start_dataset:
        logger.info(f'Calculating f.vecs. for season: {season}')

        teams = start_dataset[season]
        for team_ticker in teams:
            logger.info(f'Calculating f.vecs. for team: {team_ticker}')

            team = teams[team_ticker]
            feature_vector = {}
            feature_vectors = []

            if not os.path.exists(f'../data/feature_vector/fv_{season}_{team_ticker}.csv'):
                dataframe = pd.DataFrame(columns=FV_COLS)
                len_df_rg = 0
                len_df_pg = 0
                dataframe.to_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', index=False)
            else:
                dataframe = pd.read_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv')
                if len(dataframe) == 0:
                    len_df_rg = 0
                    len_df_pg = 0
                else:
                    len_df_rg = len(dataframe[~dataframe['playoff']]['game_id'].unique())
                    len_df_pg = len(dataframe[dataframe['playoff']]['game_id'].unique())

            for game_number in range(len_df_rg, len(team['reg_season_games'])):
                reg_game = team['reg_season_games'][game_number]
                feature_vector = {}

                logger.info(
                    f'Calculating f.vecs. for regular season game: {reg_game["game_id"]}, number: {game_number}')

                success = False
                while not success:
                    try:
                        start_time = time.time()

                        feature_vector.update(
                            get_feature_vector(season, team_ticker, reg_game['opponent'], reg_game['home'],
                                               reg_game['game_id'], False))

                        pprint(feature_vector)
                        logger.debug(
                            f'Feature vector calculation for game {reg_game["game_id"]} took {time.time() - start_time} seconds')

                        feature_vectors.append(feature_vector)
                        dataframe = pd.DataFrame(feature_vectors, columns=FV_COLS)
                        dataframe.to_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', mode='a', index=False,
                                         header=False)
                        feature_vectors = []
                        logger.debug('Feature vectors saved')
                        success = True
                    except Exception as e:
                        logger.error(f'Error occured for game {reg_game["game_id"]}')
                        logger.error(e)
                        traceback.print_exc()
                        dataframe = pd.DataFrame(feature_vectors, columns=FV_COLS)
                        dataframe.to_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', mode='a', index=False,
                                         header=False)
                        feature_vector = {}
                        feature_vectors = []
                        success = False
                        logger.debug('Feature vectors saved')
                        time.sleep(1)

            for game_number in range(len_df_pg, len(team['playoff_games'])):
                playoff_game = team['playoff_games'][game_number]
                feature_vector = {}

                logger.info(f'Calculating f.vecs. for playoff game: {playoff_game["game_id"]}, number: {game_number}')

                success = False
                while not success:
                    try:
                        start_time = time.time()

                        feature_vector.update(get_feature_vector(season, team_ticker, playoff_game['opponent'],
                                                                 playoff_game['home'], playoff_game['game_id'], True))
                        logger.debug(
                            f'Feature vector calculation for game {playoff_game["game_id"]} took {time.time() - start_time} seconds')

                        feature_vectors.append(feature_vector)
                        dataframe = pd.DataFrame(feature_vectors, columns=FV_COLS)
                        dataframe.to_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', mode='a', index=False,
                                         header=False)
                        feature_vectors = []
                        logger.debug('Feature vectors saved')
                        success = True
                    except Exception as e:
                        logger.error(f'Error occured for game {playoff_game["game_id"]}')
                        logger.error(e)
                        traceback.print_exc()
                        dataframe = pd.DataFrame(feature_vectors, columns=FV_COLS)
                        dataframe.to_csv(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', mode='a', index=False,
                                         header=False)
                        feature_vector = {}
                        feature_vectors = []
                        success = False
                        logger.debug('Feature vectors saved')
                        time.sleep(1)

            # logger.debug(f'Saving feature vectors for team {team_ticker}, season {season}')
            # with open(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', 'wb') as f:
            #     dataframe = pd.DataFrame(feature_vectors)
            #     dataframe.to_csv(f, index=False, mode='a', header=False)

