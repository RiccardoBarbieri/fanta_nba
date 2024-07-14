# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.match_stats import MatchStats  # noqa: E501
from swagger_server.models.player_stats import PlayerStats  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_stats import TeamStats  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_match_match_id_stats_get(self):
        """Test case for match_match_id_stats_get

        Retrieve match stats by match ID
        """
        query_string = [('match_date', 'match_date_example')]
        response = self.client.open(
            '/match/{match_id}/stats'.format(match_id='match_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_matches_get(self):
        """Test case for matches_get

        Retrieve all matches beetween two dates
        """
        query_string = [('date_from', 'date_from_example'),
                        ('date_to', 'date_to_example')]
        response = self.client.open(
            '/matches',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_players_player_id_stats_get(self):
        """Test case for players_player_id_stats_get

        Retrieve player stats by player ID, season, date, location and number of games
        """
        query_string = [('season', 'season_example'),
                        ('date_to', '2013-10-20'),
                        ('last_x', 56),
                        ('home_away_filter', 'home_away_filter_example')]
        response = self.client.open(
            '/players/{player_id}/stats'.format(player_id='player_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_teams_get(self):
        """Test case for teams_get

        Retrieve all teams by ticker and season
        """
        query_string = [('team_tickers', 'team_tickers_example'),
                        ('season', 'season_example')]
        response = self.client.open(
            '/teams',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_teams_team_id_stats_get(self):
        """Test case for teams_team_id_stats_get

        Retrieve team stats by team ID, season, date, number of games, and location
        """
        query_string = [('season', 'season_example'),
                        ('date_to', '2013-10-20'),
                        ('last_x', 56),
                        ('home_away_filter', 'home_away_filter_example')]
        response = self.client.open(
            '/teams/{team_id}/stats'.format(team_id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_teams_team_ticker_get(self):
        """Test case for teams_team_ticker_get

        Retrieve team information and players by ticker and season
        """
        query_string = [('season', 'season_example')]
        response = self.client.open(
            '/teams/{team_ticker}'.format(team_ticker='team_ticker_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
