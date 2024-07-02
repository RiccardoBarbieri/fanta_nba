from pprint import pprint
from typing import List, Dict, AnyStr
import sys

sys.path.append('..')

import pandas as pd
from nba_api.stats.endpoints.boxscoreadvancedv2 import BoxScoreAdvancedV2
from nba_api.stats.endpoints.leaguedashlineups import LeagueDashLineups
from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.endpoints.playbyplayv2 import PlayByPlayV2
from nba_api.live.nba.endpoints.boxscore import BoxScore
from nba_api.stats.static import teams

from utils.helper_functions import all_keys_to_lower
from utils.validation import validate_season_string, validate_team_ticker, validate_game_number


# TODO consider implementing caching for the team_game_log
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


def get_dash_lineups(team_ticker: str, opp_team_ticker: str, game_id: str, playoffs: bool) -> List:
    """
    Get the starting lineup and the bench for a specific game.

    :param team_ticker: The team abbreviation.
    :param opp_team_ticker: The opponent team abbreviation.
    :param game_id: The game identifier.
    :param playoffs: true to get the playoff games, false to get the regular season games.

    :return: A list containing the dashboard lineup for the game.
    """
    validate_team_ticker(team_ticker)

    teams_info = teams.get_teams()
    team_id = filter(lambda x: x['abbreviation'] == team_ticker, teams_info).__next__()['id']
    opp_team_id = filter(lambda x: x['abbreviation'] == opp_team_ticker, teams_info).__next__()['id']

    league_game_log = get_season_games_for_team(team_ticker, '2023-24', playoffs)
    date = filter(lambda x: x['game_id'] == game_id, league_game_log).__next__()['game_date']

    if playoffs:
        season_type = 'Playoffs'
    else:
        season_type = 'Regular Season'

    dash_lineups = LeagueDashLineups(team_id_nullable=team_id,
                                     opponent_team_id=opp_team_id,
                                     date_from_nullable=date,
                                     date_to_nullable=date,
                                     season_type_all_star=season_type).get_normalized_dict()['Lineups']

    return all_keys_to_lower(dash_lineups)


def get_boxscore_teamstats(game_id: str) -> Dict:
    """
    Get the boxscore for a specific game.

    :param game_id: The game identifier.

    :return: A dictionary containing the boxscore for the game.
    """
    boxscore = BoxScoreAdvancedV2(game_id=game_id).get_normalized_dict()['TeamStats']

    return all_keys_to_lower(boxscore)


def get_live_boxscore(game_id: str) -> Dict:
    """
    Get the live boxscore for a specific game.

    :param game_id: The game identifier.

    :return: A dictionary containing the live boxscore for the game.
    """
    boxscore = BoxScore(game_id=game_id).get_dict()['game']

    return all_keys_to_lower(boxscore)


def get_playbyplay(game_id: str) -> Dict:
    """
    Get the play by play for a specific game.

    :param game_id: The game identifier.

    :return: A dictionary containing the play by play for the game.
    """
    playbyplay = PlayByPlayV2(game_id=game_id).get_normalized_dict()['PlayByPlay']

    return all_keys_to_lower(playbyplay)


def get_prev_game(team_ticker: str, game_id: str, season: str, playoffs: bool) -> str | None:
    """
    Get the previous game played by a team in a season.

    :param team_ticker: The team abbreviation.
    :param game_id: The game identifier.
    :param season: A string representing the season in the format 'YYYY-YY'.
    :param playoffs: true to get the playoff games, false to get the regular season games.
    :return: The id of the previous game played by the team, None if there is no previous game.
    """
    validate_team_ticker(team_ticker)
    validate_season_string(season)

    team_game_log = get_season_games_for_team(team_ticker, season, playoffs)

    df_team_game_log = pd.DataFrame(team_game_log)
    if game_id not in df_team_game_log['game_id'].tolist():
        raise ValueError('Game ID not found in the game log')

    df_team_game_log.loc[:, 'game_date'] = pd.to_datetime(df_team_game_log['game_date'], format='%b %d, %Y')
    df_team_game_log.sort_values(by='game_date', inplace=True, ascending=True)
    df_team_game_log.reset_index(drop=True, inplace=True)

    game_index = df_team_game_log[df_team_game_log['game_id'] == game_id].index[0]

    if game_index == 0:
        return None

    return df_team_game_log.iloc[game_index - 1, :]['game_id']


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
# maybe it's ok to use game number system for playoffs also, get tot games for team before TODO ref 1
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

    # TODO ref 1
    # if playoffs and game_number > 16:
    #     raise ValueError('Game number must be between 1 and 16 for playoffs')

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
        'team_id': df_team_game_log.iloc[game_number - 1, :]['team_id'],  # TODO maybe replace with team_ticker
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


def get_longest_lineup(team_ticker: str, opp_team_ticker: str, game_id: str, playoffs: bool) -> Dict[
    AnyStr, List[Dict[AnyStr, AnyStr]]]:
    """
    Get the lineup that has played for the longest time and the bench calculated by eliminating that lineup from all the
    players that played in the game.

    :param team_ticker: The team abbreviation.
    :param opp_team_ticker: The opponent team abbreviation.
    :param game_id: The game identifier.
    :param playoffs: true to get the playoff games, false to get the regular season games.

    :return: A dictionary containing the starting lineup and the bench for the game, like
    {
        'lineup': [{'name': 'Player A', 'id': '123'}, ...],
        'bench': [{'name': 'Player B', 'id': '456'}, ...],
    }
    """
    dash_lineups = get_dash_lineups(team_ticker, opp_team_ticker, game_id, playoffs)

    dash_lineups.sort(key=lambda x: -x['min'])

    # Getting all players that played in the game
    all_players = set()
    for i in dash_lineups:
        all_players.update(
            [(name, id) for name, id in zip(i['group_name'].split(' - '), i['group_id'].split('-')[1:-1])])

    # Getting lineup that played the longest
    lineup_names_string = dash_lineups[0]['group_name']
    lineup_ids_string = dash_lineups[0]['group_id']
    longest_lineup = set(
        [(name, id) for name, id in zip(lineup_names_string.split(' - '), lineup_ids_string.split('-')[1:-1])])

    # Getting the bench by removing the longest lineup from all players
    bench = all_players - longest_lineup

    return {'lineup': [{'name': name, 'id': id} for name, id in longest_lineup],
            'bench': [{'name': name, 'id': id} for name, id in bench]}


def get_offdef_rating(team_ticker: str, season: str, game_id_up_to: str, playoffs: bool) -> Dict[AnyStr, float]:
    """
    Get the offensive and defensive rating for a specific game.

    :param team_ticker: The team abbreviation.
    :param game_id_up_to: The game identifier.
    :param season: A string representing the season in the format 'YYYY-YY'.
    :param playoffs: true to get the playoff games, false to get the regular season games.
    :return: A dictionary containing the offensive and defensive rating for the team.
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
        boxscores = get_boxscore_teamstats(game_id)
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

    return {'off_rating': (100 * (round(team_points) / team_poss)), 'def_rating': 100 * (round(opp_points) / opp_poss)}


def get_referee(game_id: str) -> Dict:
    """
    Get the referees for a specific game.

    :param game_id: The game identifier.

    :return: A list containing the referees for the game.
    """
    live_boxscore = get_live_boxscore(game_id)['officials']

    off1 = filter(lambda x: x['assignment'] == 'OFFICIAL1', live_boxscore).__next__()

    return {'name': off1['name'], 'id': off1['personId']}


def get_arena(game_id: str | None) -> Dict:
    """
    Get the arena for a specific game.

    :param game_id: The game identifier, if None return home arena.

    :return: A dictionary containing the arena for the game.
    """

    if game_id is None:
        team_game_log = get_season_games_for_team('BOS', '2023-24', False)
        df_team_game_log = pd.DataFrame(team_game_log)
        df_team_game_log.loc[:, 'game_date'] = pd.to_datetime(df_team_game_log['game_date'], format='%b %d, %Y')
        df_team_game_log.sort_values(by='game_date', inplace=True, ascending=True)
        df_team_game_log.reset_index(drop=True, inplace=True)
        first_home_game_id = df_team_game_log[df_team_game_log['matchup'].str.contains('vs.')].iloc[0, :]['game_id']
        game_id = first_home_game_id

    live_boxscore = get_live_boxscore(game_id)

    return {'name': live_boxscore['arena']['arenaName'], 'city': live_boxscore['arena']['arenaCity'], 'state': live_boxscore['arena']['arenaState']}


def print_df(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
        print(df)


if __name__ == '__main__':

    prev_game = get_prev_game('BOS', '0022300065', '2023-24', False)

    print(prev_game)

    print(get_arena(prev_game))
    print(get_arena('0022300065'))

    # print(teams.get_teams())
     
    #        team_id     game_id            game_date      matchup
    # 0   1610612738  0022300065  2023-10-25 00:00:00    BOS @ NYK
    # 1   1610612738  0022300080  2023-10-27 00:00:00  BOS vs. MIA
    # 2   1610612738  0022300103  2023-10-30 00:00:00    BOS @ WAS
    # 3   1610612738  0022300118  2023-11-01 00:00:00  BOS vs. IND
    # 4   1610612738  0022300136  2023-11-04 00:00:00    BOS @ BKN
    # 5   1610612738  0022300154  2023-11-06 00:00:00    BOS @ MIN
    # 6   1610612738  0022300159  2023-11-08 00:00:00    BOS @ PHI
    # 7   1610612738  0022300010  2023-11-10 00:00:00  BOS vs. BKN
    # 8   1610612738  0022300174  2023-11-11 00:00:00  BOS vs. TOR
    # 9   1610612738  0022300188  2023-11-13 00:00:00  BOS vs. NYK
    # 10  1610612738  0022300194  2023-11-15 00:00:00    BOS @ PHI
    # 11  1610612738  0022300031  2023-11-17 00:00:00    BOS @ TOR
    # 12  1610612738  0022300213  2023-11-19 00:00:00    BOS @ MEM
    # 13  1610612738  0022300217  2023-11-20 00:00:00    BOS @ CHA
    # 14  1610612738  0022300228  2023-11-22 00:00:00  BOS vs. MIL

# MISSING

# offensive and defensive rating A and B DONE
# starting lineup A and B ????? DONE
# bench A and B ????? DONE
# win percentage last 5 games A and B DONE
# referee name DONE

# distance travelled by away team PDPDPDPD

# home_team 0 if A at home, 1 if B at home TODO: apply when combining the methods
# game date TODO: apply when combining the methods
# season TODO: apply when combining the methods
# topic (if season 0, if playoffs 1) TODO: apply when combining the methods
