import sys
import swagger_server.controllers.team_controller as team_controller
import swagger_server.controllers.player_controller as player_controller
import swagger_server.controllers.match_controller as default_controller

sys.path.append('..')

HAWKS = [1610612737, "ATL", "Hawks", 1949, "Atlanta", "Atlanta Hawks", "Georgia", [1958]]

if __name__ == '__emain__':
    #result = team_controller.get_all_teams_by_ticker(["ATL", "LAL", "GSW"], "2023-24")
    #result = team_controller.get_team_by_ticker("ATL", "2023-24")
    result = team_controller.get_team_stats("1610612737", "2023-24", "2024-08-08", 5, "HOME")
    print(result)


if __name__ == '__emain__':
    result = player_controller.get_player_stats("1629027", "2023-24", "2024-08-08", 5,
                                                "HOME")
    print(result)

if __name__ == '__main__':
    #result = default_controller.get_all_match_infos([{"match-up": "GSW - UTA", "date": "2024-04-14"},{"match-up": "BKN - WAS", "date": "2024-03-27"}], "2023-24")
    #result = default_controller.get_match_info("GSW - UTA", "2024-04-14", "2023-24")
    result = default_controller.get_match_stats("0022301198", "GSW", "UTA", "2024-04-14", "2023-24")
    print(result)