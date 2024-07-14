from typing import Dict, List

import featurevec.rest_api_functions_helper as helper


# Rest Api Controller for standings

def standings_get(date: str) -> dict[str, dict | list[dict]]:
    standing = helper.get_standing_by_date(date)

    for west_team in standing["west"]:
        info = helper.get_team_base_info_by_id(west_team["team_id"])
        west_team["team"] = info["name"]
        west_team["team_ticker"] = info["ticker"]

    for east_team in standing["east"]:
        info = helper.get_team_base_info_by_id(east_team["team_id"])
        east_team["team"] = info["name"]
        east_team["team_ticker"] = info["ticker"]

    return standing
