import requests
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import drafthistory
from nba_api.stats.endpoints import cumestatsteamgames
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import leaguegamefinder
from pprint import pprint
import pandas
import json

pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 200)

game_found = leaguegamefinder.LeagueGameFinder(
    player_or_team_abbreviation="T",
    league_id_nullable="00",
    team_id_nullable=1610612738,
    game_id_nullable="0042300402",
    # date_to_nullable="06/09/2024",
    # date_from_nullable="06/08/2024",
)

with open('league_game_finder.json', 'w+') as outfile:
    json.dump(game_found.get_normalized_dict(), outfile, indent=4)
