import os.path
import pickle
import sys
from pprint import pprint
from typing import List
import pandas as pd

sys.path.append('..')

from utils.validation import validate_season_string

from nba_api.stats.static.teams import get_teams

from feature_vector_helper import get_common_team_roster, get_season_games_for_team, print_df
from utils.helper_functions import get_home_away_team, get_opponent


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
                'players': []
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
                        'home': True,
                        'opponent': 'MIL'
                    }]
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

    file_name_prefix = '../data/teams_players_by_season_'

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
                df_reg_season_games.loc[:, 'game_date'] = pd.to_datetime(df_reg_season_games['game_date'], format='%b %d, %Y')
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
                    df_playoff_games.loc[:, 'game_date'] = pd.to_datetime(df_playoff_games['game_date'], format='%b %d, %Y')
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


if __name__ == '__main__':
    seasons = ['2018-19', '2019-20', '2020-21', '2021-22', '2023-24']

    teams_players_by_season = get_starting_dataset(seasons)

    pprint(teams_players_by_season)

    # Order of function calls to get the feature vector for a player:
    # aggregate_simple_season_stats(team_ticker, season, playoffs, game_number)
    # get_referee(game_id)
    # get_distance_travelled(team_ticker, game_id, season, playoffs)
    # get_longest_lineup(team_ticker, opp_team_ticker, game_id, playoffs)
    # get_offdef_rating(team_ticker, season, game_id_up_to, playoffs)
    # get_player_efficiency(player_id, game_id_up_to, season)
