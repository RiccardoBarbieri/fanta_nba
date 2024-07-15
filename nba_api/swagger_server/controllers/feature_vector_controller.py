import time
import traceback

from featurevec.feature_vector_calculator import get_feature_vector, get_game_id_and_season_type, is_team_home


def feature_vector_get(season: str, team_ticker: str, opp_team_ticker: str, date: str) -> dict[str, any]:
    """
    Get feature vector for a given team, season, opponent team and date

    :param season: Season
    :param team_ticker: Team ticker
    :param opp_team_ticker: Opponent team ticker
    :param date: Date
    :return: Feature vector
    """
    success = False
    while not success:
        try:
            info = get_game_id_and_season_type(team_ticker, season, date)
            success = True
        except Exception as e:
            print("Error occured")
            print(e)
            traceback.print_exc()
            success = False
            time.sleep(1)

    game_id = info["game_id"]
    playoff = info["playoff"]

    success = False
    while not success:
        try:
            is_main_team_home = is_team_home(team_ticker, game_id, season)
            success = True
        except Exception as e:
            print("Error occured")
            print(e)
            traceback.print_exc()
            success = False
            time.sleep(1)

    success = False
    while not success:
        try:
            feature_vector = get_feature_vector(
                season,
                team_ticker,
                opp_team_ticker,
                is_main_team_home,
                game_id,
                playoff
            )
            success = True
        except Exception as e:
            print("Error occured")
            print(e)
            traceback.print_exc()
            success = False
            time.sleep(1)

    return feature_vector
