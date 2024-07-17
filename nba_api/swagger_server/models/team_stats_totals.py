# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TeamStatsTotals(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, wins: int=None, losses: int=None):  # noqa: E501
        """TeamStatsTotals - a model defined in Swagger

        :param wins: The wins of this TeamStatsTotals.  # noqa: E501
        :type wins: int
        :param losses: The losses of this TeamStatsTotals.  # noqa: E501
        :type losses: int
        """
        self.swagger_types = {
            'wins': int,
            'losses': int
        }

        self.attribute_map = {
            'wins': 'wins',
            'losses': 'losses'
        }
        self._wins = wins
        self._losses = losses

    @classmethod
    def from_dict(cls, dikt) -> 'TeamStatsTotals':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TeamStats_totals of this TeamStatsTotals.  # noqa: E501
        :rtype: TeamStatsTotals
        """
        return util.deserialize_model(dikt, cls)

    @property
    def wins(self) -> int:
        """Gets the wins of this TeamStatsTotals.


        :return: The wins of this TeamStatsTotals.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins: int):
        """Sets the wins of this TeamStatsTotals.


        :param wins: The wins of this TeamStatsTotals.
        :type wins: int
        """

        self._wins = wins

    @property
    def losses(self) -> int:
        """Gets the losses of this TeamStatsTotals.


        :return: The losses of this TeamStatsTotals.
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses: int):
        """Sets the losses of this TeamStatsTotals.


        :param losses: The losses of this TeamStatsTotals.
        :type losses: int
        """

        self._losses = losses