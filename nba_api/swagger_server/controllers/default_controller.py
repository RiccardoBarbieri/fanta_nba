from typing import List, Dict, Any, Tuple

from swagger_server.models.match_up import MatchUp  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.player_advanced_details import PlayerAdvancedDetails  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_advanced_detailed_statistics import TeamAdvancedDetailedStatistics  # noqa: E501
from swagger_server.models.team_advanced_details import TeamAdvancedDetails  # noqa: E501

import featurevec.rest_api_functions_helper as helper


def get_all_matchup_ids(matches, date_from, date_to):  # noqa: E501

    """Get all match-up ids

     # noqa: E501

    :param matches: array della forma LAL vs BOS
    :param x:
    :type x: int

    :rtype: "MATCHUP",
            "Game_ID"
    """

    return helper.get_game_id_and_season_type("LAL", "2023-24", "2024-04-28", "2024-04-20");


def matchup_id_advanced_get(id, x):  # noqa: E501
    """Get advanced details of a match-up

     # noqa: E501

    :param id: 
    :type id: int
    :param x: 
    :type x: int

    :rtype: List[AdvancedMatchDetails]
    """
    return 'do some magic!'


def matchup_id_get(id):  # noqa: E501
    """Get basic details of a match-up

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: MatchUp
    """
    return 'do some magic!'


def player_id_advanced_get(id, x, filter):  # noqa: E501
    """Get advanced details of a player

     # noqa: E501

    :param id: 
    :type id: int
    :param x: 
    :type x: int
    :param filter: 
    :type filter: str

    :rtype: PlayerAdvancedDetails
    """
    return 'do some magic!'


def player_id_get(id):  # noqa: E501
    """Get basic details of a player

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Player
    """
    return 'do some magic!'