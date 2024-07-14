# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.referee import Referee  # noqa: F401,E501
from swagger_server.models.team_info import TeamInfo  # noqa: F401,E501
from swagger_server import util


class Match(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, match_up: str=None, game_id: str=None, _date: date=None, home_team: TeamInfo=None, away_team: TeamInfo=None, referee: Referee=None):  # noqa: E501
        """Match - a model defined in Swagger

        :param match_up: The match_up of this Match.  # noqa: E501
        :type match_up: str
        :param game_id: The game_id of this Match.  # noqa: E501
        :type game_id: str
        :param _date: The _date of this Match.  # noqa: E501
        :type _date: date
        :param home_team: The home_team of this Match.  # noqa: E501
        :type home_team: TeamInfo
        :param away_team: The away_team of this Match.  # noqa: E501
        :type away_team: TeamInfo
        :param referee: The referee of this Match.  # noqa: E501
        :type referee: Referee
        """
        self.swagger_types = {
            'match_up': str,
            'game_id': str,
            '_date': date,
            'home_team': TeamInfo,
            'away_team': TeamInfo,
            'referee': Referee
        }

        self.attribute_map = {
            'match_up': 'match_up',
            'game_id': 'game_id',
            '_date': 'date',
            'home_team': 'home_team',
            'away_team': 'away_team',
            'referee': 'referee'
        }
        self._match_up = match_up
        self._game_id = game_id
        self.__date = _date
        self._home_team = home_team
        self._away_team = away_team
        self._referee = referee

    @classmethod
    def from_dict(cls, dikt) -> 'Match':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Match of this Match.  # noqa: E501
        :rtype: Match
        """
        return util.deserialize_model(dikt, cls)

    @property
    def match_up(self) -> str:
        """Gets the match_up of this Match.


        :return: The match_up of this Match.
        :rtype: str
        """
        return self._match_up

    @match_up.setter
    def match_up(self, match_up: str):
        """Sets the match_up of this Match.


        :param match_up: The match_up of this Match.
        :type match_up: str
        """

        self._match_up = match_up

    @property
    def game_id(self) -> str:
        """Gets the game_id of this Match.


        :return: The game_id of this Match.
        :rtype: str
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id: str):
        """Sets the game_id of this Match.


        :param game_id: The game_id of this Match.
        :type game_id: str
        """

        self._game_id = game_id

    @property
    def _date(self) -> date:
        """Gets the _date of this Match.


        :return: The _date of this Match.
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date: date):
        """Sets the _date of this Match.


        :param _date: The _date of this Match.
        :type _date: date
        """

        self.__date = _date

    @property
    def home_team(self) -> TeamInfo:
        """Gets the home_team of this Match.


        :return: The home_team of this Match.
        :rtype: TeamInfo
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team: TeamInfo):
        """Sets the home_team of this Match.


        :param home_team: The home_team of this Match.
        :type home_team: TeamInfo
        """

        self._home_team = home_team

    @property
    def away_team(self) -> TeamInfo:
        """Gets the away_team of this Match.


        :return: The away_team of this Match.
        :rtype: TeamInfo
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team: TeamInfo):
        """Sets the away_team of this Match.


        :param away_team: The away_team of this Match.
        :type away_team: TeamInfo
        """

        self._away_team = away_team

    @property
    def referee(self) -> Referee:
        """Gets the referee of this Match.


        :return: The referee of this Match.
        :rtype: Referee
        """
        return self._referee

    @referee.setter
    def referee(self, referee: Referee):
        """Sets the referee of this Match.


        :param referee: The referee of this Match.
        :type referee: Referee
        """

        self._referee = referee
