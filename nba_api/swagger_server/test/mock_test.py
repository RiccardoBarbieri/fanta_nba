import sys
import swagger_server.controllers.default_controller as controller

sys.path.append('..')

if __name__ == '__main__':
    HAWKS = [1610612737, "ATL", "Hawks", 1949, "Atlanta", "Atlanta Hawks", "Georgia", [1958]]
    result = controller.get_team_stats("1610612737", "2023-24", "2024-08-08", 5, "HOME")

    print(result)
