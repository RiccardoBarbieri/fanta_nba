import datetime
import sys
import time
from utils.helper_functions import all_keys_to_lower
from utils.validation import validate_team_ticker, validate_season_string

from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.endpoints.playergamelog import PlayerGameLog
from nba_api.stats.static import teams
from nba_api.stats.endpoints.commonteamroster import CommonTeamRoster

sys.path.append('..')


def get_game_id_and_season_type(team_ticker: str, season: str, date_from: str | None, date_to: str | None) \
        -> list[dict[str, any]]:
    """
    Get the game id of the game for the team.

    :param team_ticker: The team abbreviation.
    :param season: The season in the format 'YYYY-YY'.
    :param date_from: The start date of the range in the format 'YYYY-MM-DD' (optional).
    :param date_to: The end date of the range in the format 'YYYY-MM-DD' (optional).
    :return: A list of dicts containing the match-up, date, game id, and season type (playoffs or regular season).
    """
    if date_from is not None:
        date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d').strftime('%m/%d/%Y')
    else:
        date_from = datetime.datetime.strptime("1900-01-01", '%Y-%m-%d').strftime('%m/%d/%Y')
    if date_to is not None:
        date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y')
    else:
        date_to = datetime.datetime.strptime("2999-01-01", '%Y-%m-%d').strftime('%m/%d/%Y')

    team_id = get_team_id_from_ticker(team_ticker)
    reg_team_game_log = get_season_games_for_team_until_date_to(team_id, season, False, date_from, date_to)
    po_team_game_log = get_season_games_for_team_until_date_to(team_id, season, True, date_from, date_to)

    res = []
    if po_team_game_log is not None:
        for game in po_team_game_log:
            res.append(
                {'match-up': game['matchup'], 'date': game['game_date'], 'game_id': game['game_id'], 'season': "po"})

    if reg_team_game_log is not None:
        for game in reg_team_game_log:
            res.append(
                {'match-up': game['matchup'], 'date': game['game_date'], 'game_id': game['game_id'], 'season': "reg"})

    return res


def isvalid(key: str) -> bool:
    """
    Check if a given key is valid to be considered in game stats.

    :param key: The key to validate.
    :return: True if the key is valid, False otherwise.
    """
    if key is None or key in {"team_id", "player_id", "video_available", "w", "l", "w_pct", "min"}:
        return False
    return True


def calculate_sums_averages(data: list[dict]) \
        -> tuple[dict[any, int | float], dict[any, float]] | tuple[int, int, dict[any, float]]:
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


def get_last_games_at_home_away(match_log: list[dict[str, any]], last_x: int | None, home_away: str | None,
                                opp_team_ticker: str | None) -> list[dict[str, any]]:
    """
    Filter and return the last 'x' games based on the home/away filter.

    :param match_log: List of dictionaries representing team game logs.
    :param last_x: Number of recent games to consider (optional).
    :param home_away: Filter for home ('HOME') or away ('AWAY') games (optional).
    :param opp_team_ticker: Team ticker of the opposite team (optional)
    :return: List of dictionaries representing filtered team game logs.
    """
    if opp_team_ticker is not None:
        validate_team_ticker(opp_team_ticker)
        match_log = list(filter(lambda match_log: opp_team_ticker in match_log['matchup'], match_log))

    if home_away is not None and (home_away == "HOME" or home_away == "AWAY"):
        if home_away == "AWAY":
            match_log = list(filter(lambda match_log: '@' in match_log['matchup'], match_log))
        else:
            match_log = list(filter(lambda match_log: 'vs' in match_log['matchup'], match_log))

    if last_x is not None and last_x > 0:
        match_log = match_log[:last_x]

    return match_log


def get_all_games_for_team_until_date_to(team_id: str, season: str, date_to: str) -> list[dict[str, any]]:
    """
    Retrieve all games for a team until a specified date.

    :param team_id: The ID of the team.
    :param season: The season in the format 'YYYY-YY'.
    :param date_to: The cutoff date until which games are considered (format: 'YYYY-MM-DD').
    :return: List of dictionaries representing all games for the team until the specified date.
    """
    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y')

    reg_team_game_log = get_season_games_for_team_until_date_to(team_id, season, False, None, date_to)
    po_team_game_log = get_season_games_for_team_until_date_to(team_id, season, True, None, date_to)

    if po_team_game_log is None:
        return reg_team_game_log
    else:
        return reg_team_game_log + po_team_game_log


def get_season_games_for_team_until_date_to(team_id: str, season: str, playoffs: bool, date_from: datetime,
                                            date_to: datetime) -> list[dict[str, any]]:
    """
    Retrieve specific season games for a team until a specified date.

    :param team_id: The ID of the team.
    :param season: The season in the format 'YYYY-YY'.
    :param playoffs: Flag indicating whether to retrieve playoffs games (True) or regular season games (False).
    :param date_from: The cutoff date from which games are considered.
    :param date_to: The cutoff date until which games are considered.
    :return: List of dictionaries representing season games for the team until the specified date.
    """
    validate_season_string(season)

    if playoffs:
        season_type = 'Playoffs'
    else:
        season_type = 'Regular Season'

    team_game_log = TeamGameLog(team_id=int(team_id),
                                season=season,
                                season_type_all_star=season_type,
                                date_to_nullable=date_to,
                                date_from_nullable=date_from
                                ).get_normalized_dict()['TeamGameLog']
    time.sleep(0.3)

    return all_keys_to_lower(team_game_log)


def get_team_info_by_ticker(team_ticker: str) -> dict[str, str]:
    """
    Retrieve team information based on the team abbreviation.

    :param team_ticker: The team abbreviation (ticker).
    :return: Dictionary containing detailed information about the team.
    """
    teams_info = teams.get_teams()
    validate_team_ticker(team_ticker)
    return next(filter(lambda x: x['abbreviation'] == team_ticker, teams_info))


def get_players_by_team(team_ticker: str, season: str) -> list[dict[str, any]]:
    """
    Retrieve players information for a specific team and season.

    :param team_ticker: The team abbreviation.
    :param season: The season in the format 'YYYY-YY'.
    :return: List of dictionaries containing player information for the team.
    """
    keys_of_interest = ['PLAYER_ID', 'PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'AGE', 'EXP']

    team_id = get_team_id_from_ticker(team_ticker)
    players_data = CommonTeamRoster(team_id=team_id, season=season).get_normalized_dict()['CommonTeamRoster']

    return [{key: player[key] for key in keys_of_interest} for player in players_data]


def get_team_id_from_ticker(team_ticker: str) -> str:
    """
    Retrieve the team ID based on the team abbreviation.

    :param team_ticker: The team abbreviation.
    :return: The team ID.
    """
    teams_info = teams.get_teams()
    validate_team_ticker(team_ticker)
    return next(filter(lambda x: x['abbreviation'] == team_ticker, teams_info))['id']


def get_player_games_for_season_until_date_to(player_id: str, season: str, playoffs: bool, date_to: datetime) \
        -> list[dict[str, any]]:
    """
    Get all the games played by a player in a season.

    :param player_id: The player identifier.
    :param season: A string representing the season in the format 'YYYY-YY'.
    :param playoffs: true to get the playoff games, false to get the regular season games.
    :param date_to: The cutoff date until which games are considered.
    :return: A list of dictionaries containing the games played by the player in the season.
    """
    validate_season_string(season)

    player_game_log = PlayerGameLog(player_id=player_id, season=season,
                                    season_type_all_star='Playoffs' if playoffs else 'Regular Season',
                                    date_to_nullable=date_to).get_normalized_dict()['PlayerGameLog']

    return all_keys_to_lower(player_game_log)


def get_all_player_games_until_date_to(player_id: str, season: str, date_to: str) -> list[dict[str, any]]:
    """
    Retrieve all games for a player until a specified date.

    :param player_id: The player identifier.
    :param season: The season in the format 'YYYY-YY'.
    :param date_to: The cutoff date until which games are considered (format: 'YYYY-MM-DD').
    :return: List of dictionaries representing all games for the team until the specified date.
    """
    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y')

    reg_player_game_log = get_player_games_for_season_until_date_to(player_id, season, False, date_to)
    po_player_game_log = get_player_games_for_season_until_date_to(player_id, season, True, date_to)

    if po_player_game_log is None:
        return reg_player_game_log
    else:
        return reg_player_game_log + po_player_game_log


def get_filtered_matches_player_efficiency(filtered_stats: list[dict[str, any]]) -> float:
    """
    Get the player efficiency rating for a specific player based on selected matches.

    :param filtered_stats: The player stats in selected matches.
    :return: The player efficiency rating.
    """
    pts = 0
    ast = 0
    stl = 0
    blk = 0
    reb = 0
    missed_fg = 0
    missed_ft = 0
    tov = 0
    gp = len(filtered_stats)

    for stats in filtered_stats:
        pts += stats["pts"]
        ast += stats["ast"]
        reb += stats["reb"]
        blk += stats["blk"]
        missed_ft += stats["fta"] - stats["ftm"]
        missed_fg += stats["fga"] + stats["fg3a"] - (stats["fgm"] + stats["fg3m"])
        tov += stats["tov"]

    return (pts + reb + ast + stl + blk - (missed_fg + missed_ft + tov)) / gp
