import connexion
import six

from swagger_server.models.advanced_match_details import AdvancedMatchDetails  # noqa: E501
from swagger_server.models.match_up import MatchUp  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.player_advanced_details import PlayerAdvancedDetails  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_advanced_detailed_statistics import TeamAdvancedDetailedStatistics  # noqa: E501
from swagger_server.models.team_advanced_details import TeamAdvancedDetails  # noqa: E501
from swagger_server import util


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


def team_id_advanced_details_get(id, x, filter):  # noqa: E501
    """Get detailed advanced statistics of a team

     # noqa: E501

    :param id: 
    :type id: int
    :param x: 
    :type x: int
    :param filter: 
    :type filter: str

    :rtype: TeamAdvancedDetailedStatistics
    """
    return 'do some magic!'


def team_id_advanced_get(id, x, filter):  # noqa: E501
    """Get advanced details of a team

     # noqa: E501

    :param id: 
    :type id: int
    :param x: 
    :type x: int
    :param filter: 
    :type filter: str

    :rtype: TeamAdvancedDetails
    """
    return 'do some magic!'


def team_id_get(id):  # noqa: E501
    """Get basic details of a team

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Team
    """
    return 'do some magic!'
