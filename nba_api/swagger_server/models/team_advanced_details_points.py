# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TeamAdvancedDetailsPoints(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, scored: int=None, conceded: int=None):  # noqa: E501
        """TeamAdvancedDetailsPoints - a model defined in Swagger

        :param scored: The scored of this TeamAdvancedDetailsPoints.  # noqa: E501
        :type scored: int
        :param conceded: The conceded of this TeamAdvancedDetailsPoints.  # noqa: E501
        :type conceded: int
        """
        self.swagger_types = {
            'scored': int,
            'conceded': int
        }

        self.attribute_map = {
            'scored': 'scored',
            'conceded': 'conceded'
        }
        self._scored = scored
        self._conceded = conceded

    @classmethod
    def from_dict(cls, dikt) -> 'TeamAdvancedDetailsPoints':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TeamAdvancedDetails_points of this TeamAdvancedDetailsPoints.  # noqa: E501
        :rtype: TeamAdvancedDetailsPoints
        """
        return util.deserialize_model(dikt, cls)

    @property
    def scored(self) -> int:
        """Gets the scored of this TeamAdvancedDetailsPoints.


        :return: The scored of this TeamAdvancedDetailsPoints.
        :rtype: int
        """
        return self._scored

    @scored.setter
    def scored(self, scored: int):
        """Sets the scored of this TeamAdvancedDetailsPoints.


        :param scored: The scored of this TeamAdvancedDetailsPoints.
        :type scored: int
        """

        self._scored = scored

    @property
    def conceded(self) -> int:
        """Gets the conceded of this TeamAdvancedDetailsPoints.


        :return: The conceded of this TeamAdvancedDetailsPoints.
        :rtype: int
        """
        return self._conceded

    @conceded.setter
    def conceded(self, conceded: int):
        """Sets the conceded of this TeamAdvancedDetailsPoints.


        :param conceded: The conceded of this TeamAdvancedDetailsPoints.
        :type conceded: int
        """

        self._conceded = conceded
