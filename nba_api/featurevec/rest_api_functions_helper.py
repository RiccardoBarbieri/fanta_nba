import datetime
import functools
import time
from typing import Dict, Any, List, Tuple

import sys

sys.path.append('..')
from utils.helper_functions import all_keys_to_lower
from utils.validation import validate_season_string, validate_team_ticker

from nba_api.stats.endpoints.boxscoreadvancedv2 import BoxScoreAdvancedV2
from nba_api.stats.endpoints.leaguedashlineups import LeagueDashLineups
from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.endpoints.playbyplayv2 import PlayByPlayV2
from nba_api.stats.endpoints.scoreboardv2 import ScoreboardV2
from nba_api.stats.endpoints.boxscoresummaryv2 import BoxScoreSummaryV2
from nba_api.stats.endpoints.cumestatsplayer import CumeStatsPlayer
from nba_api.stats.endpoints.playergamelog import PlayerGameLog
from nba_api.stats.endpoints.commonplayerinfo import CommonPlayerInfo
from nba_api.stats.endpoints.commonallplayers import CommonAllPlayers
from nba_api.stats.static import teams
from nba_api.stats.endpoints.commonteamroster import CommonTeamRoster
from nba_api.stats.endpoints.leaguegamelog import LeagueGameLog
from utils.validation import validate_season_string

from nba_api.stats.static.teams import get_teams

from featurevec.feature_vector_helper import get_season_games_for_team, get_referee, \
    aggregate_simple_game_cume_stats, \
    get_longest_lineup, get_offdef_rating, get_player_efficiency, get_date_from_game_id, print_df, \
    get_league_game_log_for_season
from utils.helper_functions import get_home_away_team, get_opponent, add_suffix_to_keys
from utils.constants import LOG_FILE, FV_COLS
import featurevec.feature_vector_calculator as fvcalc


def get_game_id_and_season_type(team_ticker: str, season: str, date_to: str, date_from: str) -> Dict[str, Any]:
    """
    Get the game id of the game for the team.

    :param date_from:
    :param date_to:
    :param team_ticker: The team abbreviation.
    :param season: The season in the format 'YYYY-YY'.
    :param date: The date of the game in the format 'YYYY-MM-DD'.
    :return: A dict containing the game id and a boolean representing if the game is a playoff game.
    """

    date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')

    reg_team_game_log = get_season_games_for_team(team_ticker, season, False, date_from, date_to)
    po_team_game_log = get_season_games_for_team(team_ticker, season, True, date_from, date_to)

    for game in reg_team_game_log:
        return {'match-up': game['MATCHUP'], 'game_id': game['game_id'], 'playoff': False}

    for game in po_team_game_log:
        return {'match-up': game['MATCHUP'], 'game_id': game['game_id'], 'playoff': True}


def isvalid(key: str) -> bool:
    """
    Check if a given key is valid to be considered in game stats.

    :param key: The key to validate.
    :return: True if the key is valid, False otherwise.
    """
    if key is None or key == "team_id" or key == "w" or key == "l" or key == "w_pct" or key == "min":
        return False
    return True


def calculate_sums_averages(data: List[Dict]) -> tuple[dict[Any, int | float], dict[Any, float]] | tuple[int, int, dict[Any, float]]:
    """
    Calculate totals and averages of all given game stats.

    :param data: List of dictionaries about game stats.
    :return: A tuple containing total wins, total losses, and a dictionary of averages.
    """
    sums = {}
    averages = {}
    total_wins = 0
    total_losses = 0

    n = len(data)

    if n == 0:
        return sums, averages

    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)) and isvalid(key):
                if key in sums:
                    sums[key] += value
                else:
                    sums[key] = value
            if key == "wl":
                if value == "W":
                    total_wins += 1
                else:
                    total_losses += 1

    for key, total in sums.items():
        averages[key] = total / n

    return total_wins, total_losses, averages


def get_last_games_at_home_away(team_log: List[Dict[str, Any]], last_x: int | None, home_away: str | None) -> List[Dict[str, Any]]:
    """
    Filter and return the last 'x' games based on the home/away filter.

    :param team_log: List of dictionaries representing team game logs.
    :param last_x: Number of recent games to consider (optional).
    :param home_away: Filter for home ('HOME') or away ('AWAY') games (optional).
    :return: List of dictionaries representing filtered team game logs.
    """
    if home_away is not None and (home_away == "HOME" or home_away == "AWAY"):
        if home_away == "AWAY":
            team_log = list(filter(lambda team_log: '@' in team_log['matchup'], team_log))
        else:
            team_log = list(filter(lambda team_log: 'vs' in team_log['matchup'], team_log))

    if last_x is not None and last_x > 0:
        team_log = team_log[:last_x]

    return team_log


def get_all_games_for_team_until_date_to(team_id: str, season: str, date_to: str) -> List[Dict[str, Any]]:
    """
    Retrieve all games for a team until a specified date.

    :param team_id: The ID of the team.
    :param season: The season in the format 'YYYY-YY'.
    :param date_to: The cutoff date until which games are considered (format: 'YYYY-MM-DD').
    :return: List of dictionaries representing all games for the team until the specified date.
    """
    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y')

    reg_team_game_log = get_season_games_for_team_until_date_to(team_id, season, False, date_to)
    po_team_game_log = get_season_games_for_team_until_date_to(team_id, season, True, date_to)

    if po_team_game_log is None:
        return reg_team_game_log
    else:
        return reg_team_game_log + po_team_game_log


def get_season_games_for_team_until_date_to(team_id: str, season: str, playoffs: bool, date_to: datetime) -> List[Dict[str, Any]]:
    """
    Retrieve specific season games for a team until a specified date.

    :param team_id: The ID of the team.
    :param season: The season in the format 'YYYY-YY'.
    :param playoffs: Flag indicating whether to retrieve playoffs games (True) or regular season games (False).
    :param date_to: The cutoff date until which games are considered.
    :return: List of dictionaries representing season games for the team until the specified date.
    """
    fvcalc.validate_season_string(season)

    if playoffs:
        season_type = 'Playoffs'
    else:
        season_type = 'Regular Season'

    team_game_log = TeamGameLog(team_id=int(team_id),
                                season=season,
                                season_type_all_star=season_type,
                                date_to_nullable=date_to,
                                ).get_normalized_dict()['TeamGameLog']
    time.sleep(0.3)

    return all_keys_to_lower(team_game_log)


def get_team_info_by_ticker(team_ticker: str) -> Dict[str, str]:
    """
    Retrieve team information based on the team abbreviation.

    :param team_ticker: The team abbreviation (ticker).
    :return: Dictionary containing detailed information about the team.
    """
    teams_info = teams.get_teams()
    validate_team_ticker(team_ticker)
    return next(filter(lambda x: x['abbreviation'] == team_ticker, teams_info))


def get_all_ids_from_tickers(team_tickers: List[str]) -> List[Dict[str, str]]:
    """
    Retrieve team IDs for a list of team abbreviations (tickers).

    :param team_tickers: List of team abbreviations (tickers).
    :return: List of dictionaries, each containing the team abbreviation and its corresponding ID.
    """
    teams_info = teams.get_teams()

    result = []
    for team_ticker in team_tickers:
        validate_team_ticker(team_ticker)
        team_id = next(filter(lambda x: x['abbreviation'] == team_ticker, teams_info))['id']
        result.append({'team_ticker': team_ticker, 'team_id': team_id})

    return result


def get_team_info_by_id(team_id: str) -> Dict[str, str]:
    """
    Retrieve team information based on the team ID.

    :param team_id: The ID of the team.
    :return: Dictionary containing detailed information about the team.
    """
    teams_info = teams.get_teams()
    return next(filter(lambda x: x['id'] == team_id, teams_info))