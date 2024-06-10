import requests
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import cumestatsteamgames
from nba_api.stats.static import teams
from pprint import pprint
import pandas
import json

teams = teams.get_teams()

team_id = filter(lambda x: x['abbreviation'] == "WAS", teams).__next__()['id']
