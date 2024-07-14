# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Stat(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, season_id: str=None, team_id: int=None, team_abbreviation: str=None, team_name: str=None, game_id: str=None, game_date: date=None, match_up: str=None, wl: str=None, min: int=None, fgm: int=None, fga: int=None, fg_pct: float=None, fg3m: int=None, fg3a: int=None, fg3_pct: float=None, ftm: int=None, fta: int=None, ft_pct: float=None, oreb: int=None, dreb: int=None, reb: int=None, ast: int=None, stl: int=None, blk: int=None, tov: int=None, pf: int=None, pts: int=None, plus_minus: float=None, video_available: float=None):  # noqa: E501
        """Stat - a model defined in Swagger

        :param season_id: The season_id of this Stat.  # noqa: E501
        :type season_id: str
        :param team_id: The team_id of this Stat.  # noqa: E501
        :type team_id: int
        :param team_abbreviation: The team_abbreviation of this Stat.  # noqa: E501
        :type team_abbreviation: str
        :param team_name: The team_name of this Stat.  # noqa: E501
        :type team_name: str
        :param game_id: The game_id of this Stat.  # noqa: E501
        :type game_id: str
        :param game_date: The game_date of this Stat.  # noqa: E501
        :type game_date: date
        :param match_up: The match_up of this Stat.  # noqa: E501
        :type match_up: str
        :param wl: The wl of this Stat.  # noqa: E501
        :type wl: str
        :param min: The min of this Stat.  # noqa: E501
        :type min: int
        :param fgm: The fgm of this Stat.  # noqa: E501
        :type fgm: int
        :param fga: The fga of this Stat.  # noqa: E501
        :type fga: int
        :param fg_pct: The fg_pct of this Stat.  # noqa: E501
        :type fg_pct: float
        :param fg3m: The fg3m of this Stat.  # noqa: E501
        :type fg3m: int
        :param fg3a: The fg3a of this Stat.  # noqa: E501
        :type fg3a: int
        :param fg3_pct: The fg3_pct of this Stat.  # noqa: E501
        :type fg3_pct: float
        :param ftm: The ftm of this Stat.  # noqa: E501
        :type ftm: int
        :param fta: The fta of this Stat.  # noqa: E501
        :type fta: int
        :param ft_pct: The ft_pct of this Stat.  # noqa: E501
        :type ft_pct: float
        :param oreb: The oreb of this Stat.  # noqa: E501
        :type oreb: int
        :param dreb: The dreb of this Stat.  # noqa: E501
        :type dreb: int
        :param reb: The reb of this Stat.  # noqa: E501
        :type reb: int
        :param ast: The ast of this Stat.  # noqa: E501
        :type ast: int
        :param stl: The stl of this Stat.  # noqa: E501
        :type stl: int
        :param blk: The blk of this Stat.  # noqa: E501
        :type blk: int
        :param tov: The tov of this Stat.  # noqa: E501
        :type tov: int
        :param pf: The pf of this Stat.  # noqa: E501
        :type pf: int
        :param pts: The pts of this Stat.  # noqa: E501
        :type pts: int
        :param plus_minus: The plus_minus of this Stat.  # noqa: E501
        :type plus_minus: float
        :param video_available: The video_available of this Stat.  # noqa: E501
        :type video_available: float
        """
        self.swagger_types = {
            'season_id': str,
            'team_id': int,
            'team_abbreviation': str,
            'team_name': str,
            'game_id': str,
            'game_date': date,
            'match_up': str,
            'wl': str,
            'min': int,
            'fgm': int,
            'fga': int,
            'fg_pct': float,
            'fg3m': int,
            'fg3a': int,
            'fg3_pct': float,
            'ftm': int,
            'fta': int,
            'ft_pct': float,
            'oreb': int,
            'dreb': int,
            'reb': int,
            'ast': int,
            'stl': int,
            'blk': int,
            'tov': int,
            'pf': int,
            'pts': int,
            'plus_minus': float,
            'video_available': float
        }

        self.attribute_map = {
            'season_id': 'season_id',
            'team_id': 'team_id',
            'team_abbreviation': 'team_abbreviation',
            'team_name': 'team_name',
            'game_id': 'game_id',
            'game_date': 'game_date',
            'match_up': 'match_up',
            'wl': 'wl',
            'min': 'min',
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
            'pts': 'pts',
            'plus_minus': 'plus_minus',
            'video_available': 'video_available'
        }
        self._season_id = season_id
        self._team_id = team_id
        self._team_abbreviation = team_abbreviation
        self._team_name = team_name
        self._game_id = game_id
        self._game_date = game_date
        self._match_up = match_up
        self._wl = wl
        self._min = min
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
        self._plus_minus = plus_minus
        self._video_available = video_available

    @classmethod
    def from_dict(cls, dikt) -> 'Stat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Stat of this Stat.  # noqa: E501
        :rtype: Stat
        """
        return util.deserialize_model(dikt, cls)

    @property
    def season_id(self) -> str:
        """Gets the season_id of this Stat.


        :return: The season_id of this Stat.
        :rtype: str
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id: str):
        """Sets the season_id of this Stat.


        :param season_id: The season_id of this Stat.
        :type season_id: str
        """

        self._season_id = season_id

    @property
    def team_id(self) -> int:
        """Gets the team_id of this Stat.


        :return: The team_id of this Stat.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: int):
        """Sets the team_id of this Stat.


        :param team_id: The team_id of this Stat.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def team_abbreviation(self) -> str:
        """Gets the team_abbreviation of this Stat.


        :return: The team_abbreviation of this Stat.
        :rtype: str
        """
        return self._team_abbreviation

    @team_abbreviation.setter
    def team_abbreviation(self, team_abbreviation: str):
        """Sets the team_abbreviation of this Stat.


        :param team_abbreviation: The team_abbreviation of this Stat.
        :type team_abbreviation: str
        """

        self._team_abbreviation = team_abbreviation

    @property
    def team_name(self) -> str:
        """Gets the team_name of this Stat.


        :return: The team_name of this Stat.
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name: str):
        """Sets the team_name of this Stat.


        :param team_name: The team_name of this Stat.
        :type team_name: str
        """

        self._team_name = team_name

    @property
    def game_id(self) -> str:
        """Gets the game_id of this Stat.


        :return: The game_id of this Stat.
        :rtype: str
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id: str):
        """Sets the game_id of this Stat.


        :param game_id: The game_id of this Stat.
        :type game_id: str
        """

        self._game_id = game_id

    @property
    def game_date(self) -> date:
        """Gets the game_date of this Stat.


        :return: The game_date of this Stat.
        :rtype: date
        """
        return self._game_date

    @game_date.setter
    def game_date(self, game_date: date):
        """Sets the game_date of this Stat.


        :param game_date: The game_date of this Stat.
        :type game_date: date
        """

        self._game_date = game_date

    @property
    def match_up(self) -> str:
        """Gets the match_up of this Stat.


        :return: The match_up of this Stat.
        :rtype: str
        """
        return self._match_up

    @match_up.setter
    def match_up(self, match_up: str):
        """Sets the match_up of this Stat.


        :param match_up: The match_up of this Stat.
        :type match_up: str
        """

        self._match_up = match_up

    @property
    def wl(self) -> str:
        """Gets the wl of this Stat.


        :return: The wl of this Stat.
        :rtype: str
        """
        return self._wl

    @wl.setter
    def wl(self, wl: str):
        """Sets the wl of this Stat.


        :param wl: The wl of this Stat.
        :type wl: str
        """

        self._wl = wl

    @property
    def min(self) -> int:
        """Gets the min of this Stat.


        :return: The min of this Stat.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min: int):
        """Sets the min of this Stat.


        :param min: The min of this Stat.
        :type min: int
        """

        self._min = min

    @property
    def fgm(self) -> int:
        """Gets the fgm of this Stat.


        :return: The fgm of this Stat.
        :rtype: int
        """
        return self._fgm

    @fgm.setter
    def fgm(self, fgm: int):
        """Sets the fgm of this Stat.


        :param fgm: The fgm of this Stat.
        :type fgm: int
        """

        self._fgm = fgm

    @property
    def fga(self) -> int:
        """Gets the fga of this Stat.


        :return: The fga of this Stat.
        :rtype: int
        """
        return self._fga

    @fga.setter
    def fga(self, fga: int):
        """Sets the fga of this Stat.


        :param fga: The fga of this Stat.
        :type fga: int
        """

        self._fga = fga

    @property
    def fg_pct(self) -> float:
        """Gets the fg_pct of this Stat.


        :return: The fg_pct of this Stat.
        :rtype: float
        """
        return self._fg_pct

    @fg_pct.setter
    def fg_pct(self, fg_pct: float):
        """Sets the fg_pct of this Stat.


        :param fg_pct: The fg_pct of this Stat.
        :type fg_pct: float
        """

        self._fg_pct = fg_pct

    @property
    def fg3m(self) -> int:
        """Gets the fg3m of this Stat.


        :return: The fg3m of this Stat.
        :rtype: int
        """
        return self._fg3m

    @fg3m.setter
    def fg3m(self, fg3m: int):
        """Sets the fg3m of this Stat.


        :param fg3m: The fg3m of this Stat.
        :type fg3m: int
        """

        self._fg3m = fg3m

    @property
    def fg3a(self) -> int:
        """Gets the fg3a of this Stat.


        :return: The fg3a of this Stat.
        :rtype: int
        """
        return self._fg3a

    @fg3a.setter
    def fg3a(self, fg3a: int):
        """Sets the fg3a of this Stat.


        :param fg3a: The fg3a of this Stat.
        :type fg3a: int
        """

        self._fg3a = fg3a

    @property
    def fg3_pct(self) -> float:
        """Gets the fg3_pct of this Stat.


        :return: The fg3_pct of this Stat.
        :rtype: float
        """
        return self._fg3_pct

    @fg3_pct.setter
    def fg3_pct(self, fg3_pct: float):
        """Sets the fg3_pct of this Stat.


        :param fg3_pct: The fg3_pct of this Stat.
        :type fg3_pct: float
        """

        self._fg3_pct = fg3_pct

    @property
    def ftm(self) -> int:
        """Gets the ftm of this Stat.


        :return: The ftm of this Stat.
        :rtype: int
        """
        return self._ftm

    @ftm.setter
    def ftm(self, ftm: int):
        """Sets the ftm of this Stat.


        :param ftm: The ftm of this Stat.
        :type ftm: int
        """

        self._ftm = ftm

    @property
    def fta(self) -> int:
        """Gets the fta of this Stat.


        :return: The fta of this Stat.
        :rtype: int
        """
        return self._fta

    @fta.setter
    def fta(self, fta: int):
        """Sets the fta of this Stat.


        :param fta: The fta of this Stat.
        :type fta: int
        """

        self._fta = fta

    @property
    def ft_pct(self) -> float:
        """Gets the ft_pct of this Stat.


        :return: The ft_pct of this Stat.
        :rtype: float
        """
        return self._ft_pct

    @ft_pct.setter
    def ft_pct(self, ft_pct: float):
        """Sets the ft_pct of this Stat.


        :param ft_pct: The ft_pct of this Stat.
        :type ft_pct: float
        """

        self._ft_pct = ft_pct

    @property
    def oreb(self) -> int:
        """Gets the oreb of this Stat.


        :return: The oreb of this Stat.
        :rtype: int
        """
        return self._oreb

    @oreb.setter
    def oreb(self, oreb: int):
        """Sets the oreb of this Stat.


        :param oreb: The oreb of this Stat.
        :type oreb: int
        """

        self._oreb = oreb

    @property
    def dreb(self) -> int:
        """Gets the dreb of this Stat.


        :return: The dreb of this Stat.
        :rtype: int
        """
        return self._dreb

    @dreb.setter
    def dreb(self, dreb: int):
        """Sets the dreb of this Stat.


        :param dreb: The dreb of this Stat.
        :type dreb: int
        """

        self._dreb = dreb

    @property
    def reb(self) -> int:
        """Gets the reb of this Stat.


        :return: The reb of this Stat.
        :rtype: int
        """
        return self._reb

    @reb.setter
    def reb(self, reb: int):
        """Sets the reb of this Stat.


        :param reb: The reb of this Stat.
        :type reb: int
        """

        self._reb = reb

    @property
    def ast(self) -> int:
        """Gets the ast of this Stat.


        :return: The ast of this Stat.
        :rtype: int
        """
        return self._ast

    @ast.setter
    def ast(self, ast: int):
        """Sets the ast of this Stat.


        :param ast: The ast of this Stat.
        :type ast: int
        """

        self._ast = ast

    @property
    def stl(self) -> int:
        """Gets the stl of this Stat.


        :return: The stl of this Stat.
        :rtype: int
        """
        return self._stl

    @stl.setter
    def stl(self, stl: int):
        """Sets the stl of this Stat.


        :param stl: The stl of this Stat.
        :type stl: int
        """

        self._stl = stl

    @property
    def blk(self) -> int:
        """Gets the blk of this Stat.


        :return: The blk of this Stat.
        :rtype: int
        """
        return self._blk

    @blk.setter
    def blk(self, blk: int):
        """Sets the blk of this Stat.


        :param blk: The blk of this Stat.
        :type blk: int
        """

        self._blk = blk

    @property
    def tov(self) -> int:
        """Gets the tov of this Stat.


        :return: The tov of this Stat.
        :rtype: int
        """
        return self._tov

    @tov.setter
    def tov(self, tov: int):
        """Sets the tov of this Stat.


        :param tov: The tov of this Stat.
        :type tov: int
        """

        self._tov = tov

    @property
    def pf(self) -> int:
        """Gets the pf of this Stat.


        :return: The pf of this Stat.
        :rtype: int
        """
        return self._pf

    @pf.setter
    def pf(self, pf: int):
        """Sets the pf of this Stat.


        :param pf: The pf of this Stat.
        :type pf: int
        """

        self._pf = pf

    @property
    def pts(self) -> int:
        """Gets the pts of this Stat.


        :return: The pts of this Stat.
        :rtype: int
        """
        return self._pts

    @pts.setter
    def pts(self, pts: int):
        """Sets the pts of this Stat.


        :param pts: The pts of this Stat.
        :type pts: int
        """

        self._pts = pts

    @property
    def plus_minus(self) -> float:
        """Gets the plus_minus of this Stat.


        :return: The plus_minus of this Stat.
        :rtype: float
        """
        return self._plus_minus

    @plus_minus.setter
    def plus_minus(self, plus_minus: float):
        """Sets the plus_minus of this Stat.


        :param plus_minus: The plus_minus of this Stat.
        :type plus_minus: float
        """

        self._plus_minus = plus_minus

    @property
    def video_available(self) -> float:
        """Gets the video_available of this Stat.


        :return: The video_available of this Stat.
        :rtype: float
        """
        return self._video_available

    @video_available.setter
    def video_available(self, video_available: float):
        """Sets the video_available of this Stat.


        :param video_available: The video_available of this Stat.
        :type video_available: float
        """

        self._video_available = video_available