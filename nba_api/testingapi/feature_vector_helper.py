from pprint import pprint
from typing import List, Dict, AnyStr

import pandas as pd
from nba_api.stats.endpoints.boxscoreadvancedv2 import BoxScoreAdvancedV2
from nba_api.stats.endpoints.leaguedashlineups import LeagueDashLineups
from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.static import teams

from helper_functions import all_keys_to_lower
from validation import validate_season_string, validate_team_ticker, validate_game_number


def get_season_games_for_team(team_ticker: str, season: str, playoffs: bool) -> List[Dict]:
    """
    Get all the games played by a team in a season.

    :param playoffs: true to get the playoff games, false to get the regular season games.
    :param team_ticker: The team abbreviation.
    :param season: A string representing the season in the format 'YYYY-YY'.

    :return: A list of dictionaries containing the games played by the team in the season.
    """
    validate_season_string(season)
    validate_team_ticker(team_ticker)

    teams_info = teams.get_teams()

    team_id = filter(lambda x: x['abbreviation'] == team_ticker, teams_info).__next__()['id']

    if playoffs:
        season_type = 'Playoffs'
    else:
        season_type = 'Regular Season'

    team_game_log = TeamGameLog(team_id=team_id,
                                season=season,
                                season_type_all_star=season_type
                                ).get_normalized_dict()['TeamGameLog']

    return all_keys_to_lower(team_game_log)


def get_dash_lineups(team_ticker: str, opp_team_ticker: str, date: str, playoffs: bool) -> List:
    """
    Get the starting lineup and the bench for a specific game.

    :param team_ticker: The team abbreviation.
    :param opp_team_ticker: The opponent team abbreviation.
    :param date: The date of the game in the format 'YYYY-MM-DD'.
    :param playoffs: true to get the playoff games, false to get the regular season games.

    :return: A list containing the dashboard lineup for the game.
    """
    validate_team_ticker(team_ticker)

    teams_info = teams.get_teams()
    team_id = filter(lambda x: x['abbreviation'] == team_ticker, teams_info).__next__()['id']
    opp_team_id = filter(lambda x: x['abbreviation'] == opp_team_ticker, teams_info).__next__()['id']

    if playoffs:
        season_type = 'Playoffs'
    else:
        season_type = 'Regular Season'

    dash_lineups = LeagueDashLineups(team_id_nullable=team_id,
                                     opponent_team_id=opp_team_id,
                                     date_from_nullable=date,
                                     season_type_all_star=season_type,
                                     date_to_nullable=date).get_normalized_dict()['Lineups']

    return all_keys_to_lower(dash_lineups)


def get_boxscore(game_id: str) -> Dict:
    """
    Get the boxscore for a specific game.

    :param game_id: The game identifier.

    :return: A dictionary containing the boxscore for the game.
    """
    boxscore = BoxScoreAdvancedV2(game_id=game_id).get_normalized_dict()['TeamStats']

    return all_keys_to_lower(boxscore)


# def get_game_by_date(team_ticker: str, season: str, date: str, playoffs: bool) -> Dict:
#     """
#     Get a game played by a team in a season by date.
#
#     :param team_ticker: The team abbreviation.
#     :param season: A string representing the season in the format 'YYYY-YY'.
#     :param date: A string representing the date of the game in the format 'YYYY-MM-DD'.
#     :param playoffs: true to get the playoff games, false to get the regular season games.
#
#     :return: A dictionary containing the game played by the team in the season on the date.
#     """
#     validate_season_string(season)
#     validate_team_ticker(team_ticker)
#
#     team_game_log = get_season_games_for_team(team_ticker, season, False)
#
#     df_team_game_log = pd.DataFrame(team_game_log)
#     df_team_game_log.loc[:, 'game_date'] = pd.to_datetime(df_team_game_log['game_date'], format='%b %d, %Y')
#     df_team_game_log.sort_values(by='game_date', inplace=True, ascending=True)
#     df_team_game_log.reset_index(drop=True, inplace=True)
#     game = df_team_game_log[df_team_game_log['game_date'] == date].iloc[0, :]
#
#     return game


# TODO Create version of this function for the playoffs
# maybe it's ok to use game number system for playoffs also, get tot games for team before
def aggregate_regular_season_stats(team_ticker: str, season: str, game_number: int = 82) -> Dict:
    """
    Aggregates stats from an entire season for a specific team, the stats are aggregated
    are the one present in the team game log:
     - Wins
     - Losses
     - Field Goals Percentage
     - 3-Point Field Goals Percentage
     - Free Throws Percentage
     - Rebounds (Defensive and Offensive)
     - Assists
     - Turnovers
     - Steals
     - Blocks
     - True Shooting Percentage
     - Last 5 games win percentage

    :param game_number: The number of games to aggregate up to, default is 82, must be between 1 and 82.
    :param team_ticker: The team abbreviation.
    :param season: A string representing the season in the format 'YYYY-YY'.

    :return: A dictionary containing the combined stats of the team in the season.
    """
    validate_season_string(season)
    validate_team_ticker(team_ticker)
    validate_game_number(game_number)

    team_game_log = get_season_games_for_team(team_ticker, season, False)

    # Converting to dataframe, cleaning, sorting and grouping
    df_team_game_log = pd.DataFrame(team_game_log)
    df_team_game_log.loc[:, 'game_date'] = pd.to_datetime(df_team_game_log['game_date'], format='%b %d, %Y')
    df_team_game_log.sort_values(by='game_date', inplace=True, ascending=True)
    df_team_game_log.reset_index(drop=True, inplace=True)
    df_team_game_log = df_team_game_log.loc[:game_number - 1, :]
    # Removing unnecessary columns, only keeping the ones that are useful for the aggregation, resetting index to filter
    # on the game number
    df_team_game_log_clean = df_team_game_log.drop(
        columns=['game_id', 'game_date', 'matchup', 'wl', 'w', 'l', 'w_pct', 'fg_pct', 'fg3_pct', 'ft_pct', 'w_pct',
                 'min'])
    grouped = df_team_game_log_clean.groupby(by=['team_id']).sum()

    w_pct = df_team_game_log.iloc[game_number - 1, :]['w_pct']
    fg_pct = grouped['fgm'].sum() / grouped['fga'].sum()
    fg3_pct = grouped['fg3m'].sum() / grouped['fg3a'].sum()
    ft_pct = grouped['ftm'].sum() / grouped['fta'].sum()
    reb = grouped['oreb'].sum() + grouped['dreb'].sum()
    tot_ast = grouped['ast'].sum()
    tot_tov = grouped['tov'].sum()
    tot_stl = grouped['stl'].sum()
    tot_blk = grouped['blk'].sum()
    ts_pct = grouped['pts'].sum() / (2 * (grouped['fga'].sum() + 0.44 * grouped['fta'].sum()))
    if (game_number - 5) < 0:
        last_5_games = df_team_game_log.iloc[0:game_number, :]['wl']
        last_5_games_w_pct = last_5_games[last_5_games == 'W'].count() / game_number
    else:
        last_5_games = df_team_game_log.iloc[game_number - 5:game_number, :]['wl']
        last_5_games_w_pct = last_5_games[last_5_games == 'W'].count() / 5

    return {
        'team_id': df_team_game_log.iloc[game_number - 1, :]['team_id'],
        'season': season,
        'fg_pct': fg_pct,
        'fg3_pct': fg3_pct,
        'ft_pct': ft_pct,
        'reb': reb,
        'tot_ast': tot_ast,
        'tot_tov': tot_tov,
        'tot_stl': tot_stl,
        'tot_blk': tot_blk,
        'ts_pct': ts_pct,
        'w_pct': w_pct,
        'w_pct_last_5_games': last_5_games_w_pct
    }


# MAYBE REPLACE DATE WITH GAME_ID
def get_lineup(team_ticker: str, opp_team_ticker: str, date: str, playoffs: bool) -> List[Dict[AnyStr, AnyStr]]:
    """
    Get the starting lineup and the bench for a specific game.

    :param team_ticker: The team abbreviation.
    :param opp_team_ticker: The opponent team abbreviation.
    :param date: The date of the game in the format 'YYYY-MM-DD'.
    :param playoffs: true to get the playoff games, false to get the regular season games.

    :return: A dictionary containing the starting lineup and the bench for the game, like
    {
        'name': 'Player Name',
        'id': 'Player ID',
    }
    """
    dash_lineups = get_dash_lineups(team_ticker, opp_team_ticker, date, playoffs)

    dash_lineups.sort(key=lambda x: x['min'])

    names_string = dash_lineups[0]['group_name']
    ids_string = dash_lineups[0]['group_id']
    names = names_string.split(' - ')
    ids = ids_string.split('-')[1:-1]

    starting_lineup = [{'name': name, 'id': id} for name, id in zip(names, ids)]

    return starting_lineup


def get_offdef_rating(team_ticker: str, season: str, game_id_up_to: str, playoffs: bool) -> Dict[AnyStr, float]:
    """
    Get the offensive and defensive rating for a specific game.

    :param team_ticker: The team abbreviation.
    :param game_id_up_to: The game identifier.
    :param season: A string representing the season in the format 'YYYY-YY'.
    :param playoffs: true to get the playoff games, false to get the regular season games.
    :return:
    """
    validate_season_string(season)
    validate_team_ticker(team_ticker)

    team_game_log = get_season_games_for_team(team_ticker, season, playoffs)

    df_team_game_log = pd.DataFrame(team_game_log)
    df_team_game_log.loc[:, 'game_date'] = pd.to_datetime(df_team_game_log['game_date'], format='%b %d, %Y')
    df_team_game_log.sort_values(by='game_date', inplace=True, ascending=True)
    df_team_game_log.reset_index(drop=True, inplace=True)

    df_team_game_log = df_team_game_log.loc[:df_team_game_log[df_team_game_log['game_id'] == game_id_up_to].index[0], :]

    game_ids = df_team_game_log['game_id'].tolist()

    opp_poss = 0
    opp_points = 0

    team_poss = 0
    team_points = 0

    for game_id in game_ids:
        boxscores = get_boxscore(game_id)
        opp_boxscore = filter(lambda x: x['team_abbreviation'] != team_ticker, boxscores).__next__()
        team_boxscore = filter(lambda x: x['team_abbreviation'] == team_ticker, boxscores).__next__()


        cur_opp_poss = opp_boxscore['poss']
        cur_team_poss = team_boxscore['poss']

        opp_poss += cur_opp_poss
        team_poss += cur_team_poss

        cur_team_pts = (cur_team_poss / 100) * team_boxscore['off_rating']
        cur_opp_pts = (cur_opp_poss / 100) * opp_boxscore['off_rating']
        opp_points += cur_opp_pts
        team_points += cur_team_pts


    return {'off_rating': (100 * (int(team_points) / team_poss)), 'def_rating': 100 * (int(opp_points) / opp_poss)}


def print_df(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
        print(df)


if __name__ == '__main__':
    get_offdef_rating('BOS', '2023-24', '0022300103', False)


    #     tid         gid
    #  2  1610612738  0022300103  2023-10-30 00:00:00     BOS @ WAS
    # 74  1610612738  0022300010  2023-11-10 00:00:00   BOS vs. BKN
    # 72  1610612738  0022301060  2024-03-28 00:00:00     BOS @ ATL
    # 73  1610612738  0022301074  2024-03-30 00:00:00     BOS @ NOP

    # 74  1610612738  0022301087  2024-04-01 00:00:00     BOS @ CHA
    # 75  1610612738  0022301105  2024-04-03 00:00:00   BOS vs. OKC
    # 76  1610612738  0022301118  2024-04-05 00:00:00   BOS vs. SAC
    # 77  1610612738  0022301134  2024-04-07 00:00:00   BOS vs. POR
    # 78  1610612738  0022301148  2024-04-09 00:00:00     BOS @ MIL
    # 79  1610612738  0022301167  2024-04-11 00:00:00   BOS vs. NYK
    # 80  1610612738  0022301173  2024-04-12 00:00:00   BOS vs. CHA
    # 81  1610612738  0022301186  2024-04-14 00:00:00   BOS vs. WAS

# MISSING

# offensive and defensive rating A and B TODO already calculated in boxscoreadvancedv2
# starting lineup A and B ????? CHECK
# bench A and B ????? NOT USING
# win percentage last 5 games A and B (TODO gather from game log sorted
# referee name TODO: it is in playbyplay (maybe v2)

# home_team 0 if A at home, 1 if B at home

# distance travelled by away team

# game date TODO: apply when combining the methods
# season TODO: apply when combining the methods
# topic (if season 0, if playoffs 1) TODO: apply when combining the methods
