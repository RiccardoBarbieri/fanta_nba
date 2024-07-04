import os.path
import pickle
import sys
import time
from pprint import pprint
from typing import List, Dict, AnyStr, Any

import pandas as pd

sys.path.append('..')

from utils.validation import validate_season_string

from nba_api.stats.static.teams import get_teams

from feature_vector_helper import get_common_team_roster, get_season_games_for_team, get_referee, \
    aggregate_simple_game_cum_stats, \
    get_distance_travelled, \
    get_longest_lineup, get_offdef_rating, get_player_efficiency
from utils.helper_functions import get_home_away_team, get_opponent, add_suffix_to_keys

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


# TODO REMOVE TEAM FROM SIGNATURE, ONLY FOR LOGGING IN THIS VERSION
def get_feature_vector(season: str, team_ticker: str, opp_team_ticker: str, is_team_home: bool, game_number: int,
                       game_id: str, playoffs: bool, team: dict) -> Dict[AnyStr, Any]:
    """
    Get the feature vector for a game.

    :param season: A string representing the season in the format 'YYYY-YY'.
    :param team_ticker: A string representing the team abbreviation.
    :param opp_team_ticker: A string representing the opponent team abbreviation.
    :param is_team_home: A boolean representing if the team (not opp_team) is the home team.
    :param game_number: An integer representing the game number in the season.
    :param game_id: A string representing the game id.
    :param playoffs: A boolean representing if the game is a playoff game.
    :return: A dictionary containing the feature vector for the game.
    """

    simple_season_stats = aggregate_simple_game_cum_stats(team_ticker, season, playoffs, game_number + 1)
    distance_travelled = get_distance_travelled(team_ticker, game_id, season, playoffs)
    longest_lineup = get_longest_lineup(team_ticker, opp_team_ticker, game_id, season, playoffs)
    off_def_rating = get_offdef_rating(team_ticker, season, game_id, playoffs)

    simple_season_stats_opp = aggregate_simple_game_cum_stats(opp_team_ticker, season, playoffs, game_number + 1)
    distance_travelled_opp = get_distance_travelled(opp_team_ticker, game_id, season, playoffs)
    longest_lineup_opp = get_longest_lineup(opp_team_ticker, team_ticker, game_id, season, playoffs)
    off_def_rating_opp = get_offdef_rating(opp_team_ticker, season, game_id, playoffs)

    lineup_efficiency = 0
    for lineup_player in longest_lineup['lineup']:
        # if lineup_player not in team['players']:
        #     print(f'Player {lineup_player} from lineup is not in team {team_ticker} roster')
        lineup_efficiency += get_player_efficiency(lineup_player['id'], team_ticker, game_id, season)
    lineup_efficiency /= len(longest_lineup['lineup'])

    bench_efficiency = 0
    for bench_player in longest_lineup['bench']:
        # if bench_player not in team['players']:
        #     print(f'Player {bench_player} from bench is not in team {team_ticker} roster')
        bench_efficiency += get_player_efficiency(bench_player['id'], team_ticker, game_id, season)
    bench_efficiency /= len(longest_lineup['bench'])

    lineup_efficiency_opp = 0
    for lineup_player in longest_lineup_opp['lineup']:
        lineup_efficiency_opp += get_player_efficiency(lineup_player['id'], opp_team_ticker, game_id, season)
    lineup_efficiency_opp /= len(longest_lineup_opp['lineup'])

    bench_efficiency_opp = 0
    for bench_player in longest_lineup_opp['bench']:
        bench_efficiency_opp += get_player_efficiency(bench_player['id'], opp_team_ticker, game_id, season)
    bench_efficiency_opp /= len(longest_lineup_opp['bench'])

    misc_stats = {
        'lineup_efficiency': lineup_efficiency,
        'bench_efficiency': bench_efficiency,
        'distance_travelled': distance_travelled,
    }
    misc_stats_opp = {
        'lineup_efficiency': lineup_efficiency_opp,
        'bench_efficiency': bench_efficiency_opp,
        'distance_travelled': distance_travelled_opp,
    }

    simple_season_stats.pop('team_id')
    simple_season_stats.pop('season')

    simple_season_stats_opp.pop('team_id')
    simple_season_stats_opp.pop('season')

    # TODO create function in vector helper is_home_team(team_ticker, game_id) bool to use when this function is used in endpoint
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
        **misc_stats_opp
    }


if __name__ == '__main__':
    seasons = ['2021-22', '2022-23', '2023-24']

    start_dataset = get_starting_dataset(seasons)

    for season in start_dataset:
        print(f'Calculating f.vecs. for season: {season}')

        teams = start_dataset[season]
        for team_ticker in teams:
            # if team_ticker != 'BOS':
            #     continue

            print(f'Calculating f.vecs. for team: {team_ticker}')

            team = teams[team_ticker]
            feature_vector = {}
            feature_vectors = []
            for game_number, reg_game in enumerate(team['reg_season_games']):
                time.sleep(0.5)
                print(f'Calculating f.vecs. for regular season game: {reg_game["game_id"]}')

                feature_vector = get_feature_vector(season, team_ticker, reg_game['opponent'], reg_game['home'],
                                                    game_number, reg_game['game_id'], False, team)

                feature_vector['home_team'] = reg_game['home']
                feature_vector['season'] = season
                feature_vector['date'] = reg_game['date']
                feature_vector['playoff'] = False
                feature_vector['referee'] = get_referee(reg_game['game_id'])

                feature_vectors.append(feature_vector)

            for game_number, playoff_game in enumerate(team['playoff_games']):
                time.sleep(0.5)
                print(f'Calculating f.vecs. for playoff game: {playoff_game["game_id"]}')

                feature_vector = get_feature_vector(season, team_ticker, playoff_game['opponent'], playoff_game['home'],
                                                    game_number, playoff_game['game_id'], True, team)

                feature_vector['home_team'] = playoff_game['home']
                feature_vector['season'] = season
                feature_vector['date'] = playoff_game['date']
                feature_vector['playoff'] = True
                feature_vector['referee'] = get_referee(playoff_game['game_id'])

                feature_vectors.append(feature_vector)

            with open(f'../data/feature_vector/fv_{season}_{team_ticker}.csv', 'wb') as f:
                dataframe = pd.DataFrame(feature_vectors)
                dataframe.to_csv(f, index=False)




# Function calls to get the feature vector for a player:
# aggregate_simple_season_stats(team_ticker, season, playoffs, game_number)
# get_referee(game_id)
# get_distance_travelled(team_ticker, game_id, season, playoffs)
# get_longest_lineup(team_ticker, opp_team_ticker, game_id, playoffs)
# get_offdef_rating(team_ticker, season, game_id_up_to, playoffs)
# get_player_efficiency(player_id, game_id_up_to, season)
