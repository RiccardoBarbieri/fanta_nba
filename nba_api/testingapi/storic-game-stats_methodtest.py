from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.static import teams
from utils.helper_functions import join_to_game_info, all_keys_to_lower
import json
import re
import datetime

# Endpoint parameters:
# - team1_ticker (string) the team abbreviation
# - team2_ticker (string) the team abbreviation
# - fromdate (date string) ISO 8601 (YYYY/MM/DD) to convert to MM/DD/YYYY to use with nba-api
# - todate (date string) ISO 8601 (YYYY/MM/DD) to convert to MM/DD/YYYY to use with nba-api

# Endpoint parameters
dateFrom = '2024-01-01'
dateTo = '2024-06-06'
teamTicker1 = 'BOS'
teamTicker2 = 'WAS'

teams_info = teams.get_teams()

ticker1_id = filter(lambda x: x['abbreviation'] == teamTicker1, teams_info).__next__()['id']
ticker2_id = filter(lambda x: x['abbreviation'] == teamTicker2, teams_info).__next__()['id']

# convert to MM/DD/YYYY using datetime
date_from = datetime.datetime.strptime(dateFrom, '%Y-%m-%d').strftime('%m/%d/%Y')
date_to = datetime.datetime.strptime(dateTo, '%Y-%m-%d').strftime('%m/%d/%Y')

# Getting Boston Celtics games
ticker1_game_log = TeamGameLog(team_id=ticker1_id,
                               date_to_nullable=date_to,
                               date_from_nullable=date_from
                               ).get_normalized_dict()['TeamGameLog']

# Getting Washington Wizards games
ticker2_game_log = TeamGameLog(team_id=ticker2_id,
                               date_to_nullable=date_to,
                               date_from_nullable=date_from
                               ).get_normalized_dict()['TeamGameLog']

ticker1_game_log = all_keys_to_lower(ticker1_game_log)
ticker2_game_log = all_keys_to_lower(ticker2_game_log)

# (BOS|WAS) (vs.|@) (BOS|WAS)
re.compile(rf'({teamTicker1}|{teamTicker2}) (vs.|@) ({teamTicker1}|{teamTicker2})')

ticker1_games = list(
    filter(lambda x: re.match(rf'{teamTicker1} (vs.|@) {teamTicker2}', x['matchup']), ticker1_game_log))
ticker2_games = list(
    filter(lambda x: re.match(rf'{teamTicker2} (vs.|@) {teamTicker1}', x['matchup']), ticker2_game_log))

# Sanity checks, both lists should have the same length and same game_ids
if len(ticker1_games) != len(ticker2_games):
    raise ValueError('Both lists should have the same amount of games')

if set([i['game_id'] for i in ticker1_games]) != set([i['game_id'] for i in ticker2_games]):
    raise ValueError('Both lists should have the same games')

# Sorting both lists by game_id to join them correctly
ticker1_games = sorted(ticker1_games, key=lambda x: x['game_id'])
ticker2_games = sorted(ticker2_games, key=lambda x: x['game_id'])

with open('game_log_ticker1.json', 'w+') as f:
    json.dump(ticker1_games, f, indent=4)

with open('game_log_ticker2.json', 'w+') as f:
    json.dump(ticker2_games, f, indent=4)

# Joining games
joined_games = [join_to_game_info(ticker1_games[i], ticker2_games[i]) for i in range(len(ticker1_games))]

with open('joined_games.json', 'w+') as f:
    json.dump(joined_games, f, indent=4)

