# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.advanced_match_details import AdvancedMatchDetails  # noqa: E501
from swagger_server.models.match_up import MatchUp  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.player_advanced_details import PlayerAdvancedDetails  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_advanced_detailed_statistics import TeamAdvancedDetailedStatistics  # noqa: E501
from swagger_server.models.team_advanced_details import TeamAdvancedDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_matchup_id_advanced_get(self):
        """Test case for matchup_id_advanced_get

        Get advanced details of a match-up
        """
        query_string = [('x', 56)]
        response = self.client.open(
            '/matchup/{id}/advanced'.format(id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_matchup_id_get(self):
        """Test case for matchup_id_get

        Get basic details of a match-up
        """
        response = self.client.open(
            '/matchup/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_player_id_advanced_get(self):
        """Test case for player_id_advanced_get

        Get advanced details of a player
        """
        query_string = [('x', 56),
                        ('filter', 'filter_example')]
        response = self.client.open(
            '/player/{id}/advanced'.format(id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_player_id_get(self):
        """Test case for player_id_get

        Get basic details of a player
        """
        response = self.client.open(
            '/player/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_team_id_advanced_details_get(self):
        """Test case for team_id_advanced_details_get

        Get detailed advanced statistics of a team
        """
        query_string = [('x', 56),
                        ('filter', 'filter_example')]
        response = self.client.open(
            '/team/{id}/advanced/details'.format(id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_team_id_advanced_get(self):
        """Test case for team_id_advanced_get

        Get advanced details of a team
        """
        query_string = [('x', 56),
                        ('filter', 'filter_example')]
        response = self.client.open(
            '/team/{id}/advanced'.format(id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_team_id_get(self):
        """Test case for team_id_get

        Get basic details of a team
        """
        response = self.client.open(
            '/team/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
