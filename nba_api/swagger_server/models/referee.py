# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Referee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, id: int=None):  # noqa: E501
        """Referee - a model defined in Swagger

        :param name: The name of this Referee.  # noqa: E501
        :type name: str
        :param id: The id of this Referee.  # noqa: E501
        :type id: int
        """
        self.swagger_types = {
            'name': str,
            'id': int
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id'
        }
        self._name = name
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'Referee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Referee of this Referee.  # noqa: E501
        :rtype: Referee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Referee.


        :return: The name of this Referee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Referee.


        :param name: The name of this Referee.
        :type name: str
        """

        self._name = name

    @property
    def id(self) -> int:
        """Gets the id of this Referee.


        :return: The id of this Referee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Referee.


        :param id: The id of this Referee.
        :type id: int
        """

        self._id = id