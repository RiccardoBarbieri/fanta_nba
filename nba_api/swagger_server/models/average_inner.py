# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AverageInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, fgm: int=None, fga: int=None, fg_pct: float=None, fg3m: float=None, fg3a: float=None, fg3_pct: float=None, ftm: float=None, fta: float=None, ft_pct: float=None, oreb: float=None, dreb: float=None, reb: float=None, ast: float=None, stl: float=None, blk: float=None, tov: float=None, pf: float=None, pts: float=None):  # noqa: E501
        """AverageInner - a model defined in Swagger

        :param fgm: The fgm of this AverageInner.  # noqa: E501
        :type fgm: int
        :param fga: The fga of this AverageInner.  # noqa: E501
        :type fga: int
        :param fg_pct: The fg_pct of this AverageInner.  # noqa: E501
        :type fg_pct: float
        :param fg3m: The fg3m of this AverageInner.  # noqa: E501
        :type fg3m: float
        :param fg3a: The fg3a of this AverageInner.  # noqa: E501
        :type fg3a: float
        :param fg3_pct: The fg3_pct of this AverageInner.  # noqa: E501
        :type fg3_pct: float
        :param ftm: The ftm of this AverageInner.  # noqa: E501
        :type ftm: float
        :param fta: The fta of this AverageInner.  # noqa: E501
        :type fta: float
        :param ft_pct: The ft_pct of this AverageInner.  # noqa: E501
        :type ft_pct: float
        :param oreb: The oreb of this AverageInner.  # noqa: E501
        :type oreb: float
        :param dreb: The dreb of this AverageInner.  # noqa: E501
        :type dreb: float
        :param reb: The reb of this AverageInner.  # noqa: E501
        :type reb: float
        :param ast: The ast of this AverageInner.  # noqa: E501
        :type ast: float
        :param stl: The stl of this AverageInner.  # noqa: E501
        :type stl: float
        :param blk: The blk of this AverageInner.  # noqa: E501
        :type blk: float
        :param tov: The tov of this AverageInner.  # noqa: E501
        :type tov: float
        :param pf: The pf of this AverageInner.  # noqa: E501
        :type pf: float
        :param pts: The pts of this AverageInner.  # noqa: E501
        :type pts: float
        """
        self.swagger_types = {
            'fgm': int,
            'fga': int,
            'fg_pct': float,
            'fg3m': float,
            'fg3a': float,
            'fg3_pct': float,
            'ftm': float,
            'fta': float,
            'ft_pct': float,
            'oreb': float,
            'dreb': float,
            'reb': float,
            'ast': float,
            'stl': float,
            'blk': float,
            'tov': float,
            'pf': float,
            'pts': float
        }

        self.attribute_map = {
            'fgm': 'fgm',
            'fga': 'fga',
            'fg_pct': 'fg_pct',
            'fg3m': 'fg3m',
            'fg3a': 'fg3a',
            'fg3_pct': 'fg3_pct',
            'ftm': 'ftm',
            'fta': 'fta',
            'ft_pct': 'ft_pct',
            'oreb': 'oreb',
            'dreb': 'dreb',
            'reb': 'reb',
            'ast': 'ast',
            'stl': 'stl',
            'blk': 'blk',
            'tov': 'tov',
            'pf': 'pf',
            'pts': 'pts'
        }
        self._fgm = fgm
        self._fga = fga
        self._fg_pct = fg_pct
        self._fg3m = fg3m
        self._fg3a = fg3a
        self._fg3_pct = fg3_pct
        self._ftm = ftm
        self._fta = fta
        self._ft_pct = ft_pct
        self._oreb = oreb
        self._dreb = dreb
        self._reb = reb
        self._ast = ast
        self._stl = stl
        self._blk = blk
        self._tov = tov
        self._pf = pf
        self._pts = pts

    @classmethod
    def from_dict(cls, dikt) -> 'AverageInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Average_inner of this AverageInner.  # noqa: E501
        :rtype: AverageInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fgm(self) -> int:
        """Gets the fgm of this AverageInner.


        :return: The fgm of this AverageInner.
        :rtype: int
        """
        return self._fgm

    @fgm.setter
    def fgm(self, fgm: int):
        """Sets the fgm of this AverageInner.


        :param fgm: The fgm of this AverageInner.
        :type fgm: int
        """

        self._fgm = fgm

    @property
    def fga(self) -> int:
        """Gets the fga of this AverageInner.


        :return: The fga of this AverageInner.
        :rtype: int
        """
        return self._fga

    @fga.setter
    def fga(self, fga: int):
        """Sets the fga of this AverageInner.


        :param fga: The fga of this AverageInner.
        :type fga: int
        """

        self._fga = fga

    @property
    def fg_pct(self) -> float:
        """Gets the fg_pct of this AverageInner.


        :return: The fg_pct of this AverageInner.
        :rtype: float
        """
        return self._fg_pct

    @fg_pct.setter
    def fg_pct(self, fg_pct: float):
        """Sets the fg_pct of this AverageInner.


        :param fg_pct: The fg_pct of this AverageInner.
        :type fg_pct: float
        """

        self._fg_pct = fg_pct

    @property
    def fg3m(self) -> float:
        """Gets the fg3m of this AverageInner.


        :return: The fg3m of this AverageInner.
        :rtype: float
        """
        return self._fg3m

    @fg3m.setter
    def fg3m(self, fg3m: float):
        """Sets the fg3m of this AverageInner.


        :param fg3m: The fg3m of this AverageInner.
        :type fg3m: float
        """

        self._fg3m = fg3m

    @property
    def fg3a(self) -> float:
        """Gets the fg3a of this AverageInner.


        :return: The fg3a of this AverageInner.
        :rtype: float
        """
        return self._fg3a

    @fg3a.setter
    def fg3a(self, fg3a: float):
        """Sets the fg3a of this AverageInner.


        :param fg3a: The fg3a of this AverageInner.
        :type fg3a: float
        """

        self._fg3a = fg3a

    @property
    def fg3_pct(self) -> float:
        """Gets the fg3_pct of this AverageInner.


        :return: The fg3_pct of this AverageInner.
        :rtype: float
        """
        return self._fg3_pct

    @fg3_pct.setter
    def fg3_pct(self, fg3_pct: float):
        """Sets the fg3_pct of this AverageInner.


        :param fg3_pct: The fg3_pct of this AverageInner.
        :type fg3_pct: float
        """

        self._fg3_pct = fg3_pct

    @property
    def ftm(self) -> float:
        """Gets the ftm of this AverageInner.


        :return: The ftm of this AverageInner.
        :rtype: float
        """
        return self._ftm

    @ftm.setter
    def ftm(self, ftm: float):
        """Sets the ftm of this AverageInner.


        :param ftm: The ftm of this AverageInner.
        :type ftm: float
        """

        self._ftm = ftm

    @property
    def fta(self) -> float:
        """Gets the fta of this AverageInner.


        :return: The fta of this AverageInner.
        :rtype: float
        """
        return self._fta

    @fta.setter
    def fta(self, fta: float):
        """Sets the fta of this AverageInner.


        :param fta: The fta of this AverageInner.
        :type fta: float
        """

        self._fta = fta

    @property
    def ft_pct(self) -> float:
        """Gets the ft_pct of this AverageInner.


        :return: The ft_pct of this AverageInner.
        :rtype: float
        """
        return self._ft_pct

    @ft_pct.setter
    def ft_pct(self, ft_pct: float):
        """Sets the ft_pct of this AverageInner.


        :param ft_pct: The ft_pct of this AverageInner.
        :type ft_pct: float
        """

        self._ft_pct = ft_pct

    @property
    def oreb(self) -> float:
        """Gets the oreb of this AverageInner.


        :return: The oreb of this AverageInner.
        :rtype: float
        """
        return self._oreb

    @oreb.setter
    def oreb(self, oreb: float):
        """Sets the oreb of this AverageInner.


        :param oreb: The oreb of this AverageInner.
        :type oreb: float
        """

        self._oreb = oreb

    @property
    def dreb(self) -> float:
        """Gets the dreb of this AverageInner.


        :return: The dreb of this AverageInner.
        :rtype: float
        """
        return self._dreb

    @dreb.setter
    def dreb(self, dreb: float):
        """Sets the dreb of this AverageInner.


        :param dreb: The dreb of this AverageInner.
        :type dreb: float
        """

        self._dreb = dreb

    @property
    def reb(self) -> float:
        """Gets the reb of this AverageInner.


        :return: The reb of this AverageInner.
        :rtype: float
        """
        return self._reb

    @reb.setter
    def reb(self, reb: float):
        """Sets the reb of this AverageInner.


        :param reb: The reb of this AverageInner.
        :type reb: float
        """

        self._reb = reb

    @property
    def ast(self) -> float:
        """Gets the ast of this AverageInner.


        :return: The ast of this AverageInner.
        :rtype: float
        """
        return self._ast

    @ast.setter
    def ast(self, ast: float):
        """Sets the ast of this AverageInner.


        :param ast: The ast of this AverageInner.
        :type ast: float
        """

        self._ast = ast

    @property
    def stl(self) -> float:
        """Gets the stl of this AverageInner.


        :return: The stl of this AverageInner.
        :rtype: float
        """
        return self._stl

    @stl.setter
    def stl(self, stl: float):
        """Sets the stl of this AverageInner.


        :param stl: The stl of this AverageInner.
        :type stl: float
        """

        self._stl = stl

    @property
    def blk(self) -> float:
        """Gets the blk of this AverageInner.


        :return: The blk of this AverageInner.
        :rtype: float
        """
        return self._blk

    @blk.setter
    def blk(self, blk: float):
        """Sets the blk of this AverageInner.


        :param blk: The blk of this AverageInner.
        :type blk: float
        """

        self._blk = blk

    @property
    def tov(self) -> float:
        """Gets the tov of this AverageInner.


        :return: The tov of this AverageInner.
        :rtype: float
        """
        return self._tov

    @tov.setter
    def tov(self, tov: float):
        """Sets the tov of this AverageInner.


        :param tov: The tov of this AverageInner.
        :type tov: float
        """

        self._tov = tov

    @property
    def pf(self) -> float:
        """Gets the pf of this AverageInner.


        :return: The pf of this AverageInner.
        :rtype: float
        """
        return self._pf

    @pf.setter
    def pf(self, pf: float):
        """Sets the pf of this AverageInner.


        :param pf: The pf of this AverageInner.
        :type pf: float
        """

        self._pf = pf

    @property
    def pts(self) -> float:
        """Gets the pts of this AverageInner.


        :return: The pts of this AverageInner.
        :rtype: float
        """
        return self._pts

    @pts.setter
    def pts(self, pts: float):
        """Sets the pts of this AverageInner.


        :param pts: The pts of this AverageInner.
        :type pts: float
        """

        self._pts = pts