from typing import List, AnyStr, Dict
import sys

sys.path.append('..')

from utils.constants import LEAGUE_GAME_FINDER_FIELDS

# Static variables, to put in a CONSTANTS module
# Relevant fields from LeagueGameFinder dictionary

# Helper functions


def get_home_away_team(matchups: AnyStr) -> Dict[AnyStr, AnyStr]:
    """
    Get the home and away teams from a matchup string.

    :param matchups: A string representing a matchup.
    :return: A dictionary containing the home and away teams (home_team and away_team keys).
    """
    if ' vs. ' in matchups:
        home_team, away_team = matchups.split(' vs. ')
    elif ' @ ' in matchups:
        away_team, home_team = matchups.split(' @ ')
    else:
        raise ValueError('Matchup string must contain either " vs. " or " @ "')
    return {'home_team': home_team, 'away_team': away_team}


def all_keys_to_lower(d: Dict | List[Dict]) -> Dict | List[Dict]:
    """
    Convert all keys in a dictionary or list of dictionaries to lowercase.

    :param d: A dictionary or list of dictionaries.
    :return: A dictionary or list of dictionaries with all keys in lowercase.
    """
    if isinstance(d, list) and d and isinstance(d[0], dict):
        return [all_keys_to_lower(i) for i in d]
    elif isinstance(d, dict):
        return {k.lower(): v for k, v in d.items()}


# Main functions


def join_to_game_info(game1: Dict, game2: Dict) -> Dict:
    """
    Join two game stats dictionaries about the same game, resulting dict will have all relevant
     stats preceded by home_ and away_.
    The function expects two dict gathered from the nba_api.stats.endpoints.teamgamelog.TeamGameLog endpoint.

    :param game1: A dictionary representing the stats of a game.
    :param game2: A dictionary representing the stats of a game.
    :return: A dictionary containing the stats of both games.
    """
    game1 = all_keys_to_lower(game1)
    game2 = all_keys_to_lower(game2)

    matchup = game1['matchup']
    home_team, away_team = get_home_away_team(matchup).values()

    # Differentiating between home and away dictionaries
    home_dict = game1 if game1['matchup'].startswith(home_team) else game2
    away_dict = game1 if game1['matchup'].startswith(away_team) else game2

    # Setting generale game info
    game_info = {}
    game_info['id'] = home_dict['game_id']
    game_info['date'] = home_dict['game_date']
    game_info['home_team_id'] = home_dict['team_id']
    game_info['away_team_id'] = away_dict['team_id']
    game_info['winner'] = home_team if home_dict['wl'] == 'W' else away_team
    game_info['home_wins_until_game'] = home_dict['w']
    game_info['home_losses_until_game'] = home_dict['l']
    game_info['away_wins_until_game'] = away_dict['w']
    game_info['away_losses_until_game'] = away_dict['l']

    # Setting home and away stats
    for field in LEAGUE_GAME_FINDER_FIELDS:
        game_info[f"home_{field}"] = home_dict[field]
        game_info[f"away_{field}"] = away_dict[field]

    return game_info
