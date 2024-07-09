import sys
import swagger_server.controllers.team_controller as team_controller

sys.path.append('..')

if __name__ == '__main__':
    HAWKS = [1610612737, "ATL", "Hawks", 1949, "Atlanta", "Atlanta Hawks", "Georgia", [1958]]
    result = team_controller.get_team_stats("1610612737", "2023-24", "2024-08-08", 5, "HOME")

    print(result)
