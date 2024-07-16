import os
import time
import traceback
import requests

from featurevec.feature_vector_calculator import get_feature_vector, get_game_id_and_season_type, is_team_home

from utils.constants import FV_COLS


def get_empty_feature_vector():
    empty_fv = {}
    for i in FV_COLS:
        empty_fv.update({i: None})

    return empty_fv


def feature_vector_get(season: str, team_ticker: str, opp_team_ticker: str, date: str) -> dict[str, any]:
    """
    Get feature vector for a given team, season, opponent team and date

    :param season: Season
    :param team_ticker: Team ticker
    :param opp_team_ticker: Opponent team ticker
    :param date: Date
    :return: Feature vector
    """
    max_retries = 5

    success = False
    retries = 0
    while not success and retries < max_retries:
        try:
            info = get_game_id_and_season_type(team_ticker, season, date)
            success = True
        except Exception as e:
            print("Error occured")
            print(e)
            traceback.print_exc()
            success = False
            time.sleep(1)
            retries += 1

    game_id = info["game_id"]
    playoff = info["playoff"]

    success = False
    retries = 0
    while not success and retries < max_retries:
        try:
            is_main_team_home = is_team_home(team_ticker, game_id, season)
            success = True
        except Exception as e:
            print("Error occured")
            print(e)
            traceback.print_exc()
            success = False
            time.sleep(1)
            retries += 1

    feature_vector = get_empty_feature_vector()
    success = False
    retries = 0
    while not success and retries < max_retries:
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
            retries += 1

    return feature_vector


def score_get(feature_vector: dict[str, any]):
    """
    Get score for a given feature vector

    :param feature_vector: Feature vector
    :return: Score
    """
    url = 'https://fanta-nba-mlw-uuyto.westeurope.inference.ml.azure.com/score'
    apiKey = os.getenv('ML_API_KEY')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {apiKey}'
    }
    obj = {'data': feature_vector}

    response = requests.post(url, headers=headers, json=obj)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None

    return float(response.json()[0])
