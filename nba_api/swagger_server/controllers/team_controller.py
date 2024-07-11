import featurevec.rest_api_functions_helper as helper

# Rest Api Controller for team information and statistics


def get_team_stats(team_id: str, season: str, date_to: str, last_x: int | None, home_away_filter: str | None) -> (
        dict)[str, list[dict]]:
    """
    Retrieve team statistics based on provided parameters.

    :param team_id: The ID of the team.
    :param season: The season in the format 'YYYY-YY'.
    :param date_to: The cutoff date until which games are considered.
    :param last_x: Optional filter for the number of recent games to consider.
    :param home_away_filter: Optional filter for home ('HOME') or away ('AWAY') games.
    :return: A dictionary containing filtered game statistics, total wins and losses, and averages.
    """

    all_stats = helper.get_all_games_for_team_until_date_to(team_id, season, date_to)
    filtered_stats = helper.get_last_games_at_home_away(all_stats, last_x, home_away_filter, None)

    total_wins, total_losses, averages = helper.calculate_sums_averages(filtered_stats)

    return {
        "all_stats": filtered_stats,
        "totals": {"wins": total_wins, "losses": total_losses},
        "average": averages
    }


def get_team_by_ticker(team_ticker: str, season: str) -> dict[str, dict[str, str]]:
    """
    Retrieve team information based on the team abbreviation.

    :param team_ticker: The team abbreviation (ticker) e.g. LAL.
    :param season: The season in the format 'YYYY-YY'.
    :return: A dictionary containing the team abbreviation as key and detailed team info as value.
    """

    team_info = helper.get_team_info_by_ticker(team_ticker)
    team_players = helper.get_players_by_team(team_ticker, season)
    return {'team_ticker': team_ticker, 'team_info': team_info, 'team_players': team_players}


def get_all_teams_by_ticker(team_tickers: list[str], season: str) -> list[dict[str, dict[str, str]]]:
    """
    Retrieve information for multiple teams based on their abbreviations.

    :param team_tickers: List of team abbreviations (tickers) e.g. {BOS, LAL, MIA}.
    :param season: The season in the format 'YYYY-YY'.
    :return: A list of dictionaries, each containing the team abbreviation as key and detailed team info as value.
    """

    result = []
    for team_ticker in team_tickers:
        team_info = get_team_by_ticker(team_ticker, season)
        result.append(team_info)

    return result
