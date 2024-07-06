import re
from nba_api.stats.static import teams


def validate_season_string(season: str):
    if not re.match(r'\d{4}-\d{2}', season):
        raise ValueError(f'"{season}" is invalid. Season must be in the format YYYY-YY')
    if not season[-2:] == str(int(season[:4]) + 1)[-2:]:
        raise ValueError(f'"{season}" is invalid. Season must be in the format YYYY-YY')


def validate_team_ticker(team_ticker: str):
    if not team_ticker in [team['abbreviation'] for team in teams.get_teams()]:
        raise ValueError(f'{team_ticker} is invalid. Team ticker must be a valid NBA team abbreviation')


def validate_game_number(game_number: int):
    if game_number < 1 or game_number > 82:
        raise ValueError('Game number must be between 1 and 82')