from nba_api.stats.static import teams

teams = teams.get_teams()

team_id = filter(lambda x: x['abbreviation'] == "WAS", teams).__next__()['id']
