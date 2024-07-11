import featurevec.feature_vector_helper as feature_vector_helper
import featurevec.rest_api_functions_helper as helper


def get_all_match_infos(home_away_tickers_date: list[dict[str, str]], season: str) -> list[dict[str, str]]:
    """
    Retrieve match information for a list of home and away tickers with dates

    :param home_away_tickers_date: List of dictionaries containing home and away team tickers and dates.
    :param season: The season in the format 'YYYY-YY'.
    :return: List of dictionaries containing detailed match information for each match.
    """
    res = []
    for item in home_away_tickers_date:
        res.append(get_match_info(item["match-up"], item["date"], season))
    return res


def get_match_info(home_away_ticker: str, match_date: str, season: str) -> dict[str, str]:
    """
    Retrieve match information for a specific home and away team ticker on a given date.

    :param home_away_ticker: String in the format 'HOME_TEAM - AWAY_TEAM'.
    :param match_date: The date of the match in the format 'YYYY-MM-DD'.
    :param season: The season in the format 'YYYY-YY'.
    :return: Dictionary containing detailed match information.
    """
    home_ticker = home_away_ticker.split("-")[0].strip()
    away_ticker = home_away_ticker.split("-")[1].strip()
    matches = helper.get_game_id_and_season_type(home_ticker, season, match_date, match_date)
    for match in matches:
        game_id = match["game_id"]
        matchup = home_away_ticker
        home_team = helper.get_team_info_by_ticker(home_ticker)
        away_team = helper.get_team_info_by_ticker(away_ticker)

        referee = feature_vector_helper.get_referee(game_id)
        arena = feature_vector_helper.get_arena_by_id(game_id)
        if "vs" + away_ticker in match["match-up"]:
            matchup = home_ticker + " vs " + away_ticker
        elif "@" + away_ticker in match["match-up"]:
            matchup = away_ticker + " vs " + home_ticker

        return {"match-up": matchup, "game_id": game_id, "date": match["date"], "home_team": home_team,
                "away_team": away_team, "referee": referee, "arena": arena}


def calculate_stats(match_stats: dict[str, any], away_points: int) -> dict[str, any]:
    """
    Calculate match statistics.

    :param match_stats: Dictionary containing match statistics.
    :param away_points: Points scored by the away team.
    :return: Dictionary containing calculated match statistics.
    """
    return {"game_id": match_stats["game_id"],
            "game_date": match_stats["game_date"],
            "matchup": match_stats["matchup"],
            "winner": match_stats["matchup"][:3] if match_stats["wl"] == "W" else match_stats["matchup"][-3:],
            "home_point": match_stats["pts"],
            "away_point": away_points}


def get_match_stats(match_id: str, home_team_ticker: str, away_team_ticker: str, match_date: str, season: str) \
        -> dict[str, any]:
    """
    Retrieve match statistics for a specific match.

    :param match_id: The ID of the match.
    :param home_team_ticker: The ticker of the home team.
    :param away_team_ticker: The ticker of the away team.
    :param match_date: The date of the match in the format 'YYYY-MM-DD'.
    :param season: The season in the format 'YYYY-YY'.
    :return: Dictionary containing actual and last match statistics.
    """
    home_team_id = helper.get_team_id_from_ticker(home_team_ticker)
    away_team_id = helper.get_team_id_from_ticker(away_team_ticker)

    all_stats_by_home = helper.get_all_games_for_team_until_date_to(home_team_id, season, match_date)
    filtered_stats_by_home = helper.get_last_games_at_home_away(all_stats_by_home, None, None, away_team_ticker)

    all_stats_by_away = helper.get_all_games_for_team_until_date_to(away_team_id, season, match_date)
    filtered_stats_by_away = helper.get_last_games_at_home_away(all_stats_by_away, None, None, home_team_ticker)

    actual_match_stats_by_home = None
    actual_match_stats_by_away = None

    if filtered_stats_by_home is not None and filtered_stats_by_home[0]["game_id"] == match_id:
        actual_match_stats_by_home = filtered_stats_by_home[0]
        filtered_stats_by_home.pop(0)

    if filtered_stats_by_away is not None and filtered_stats_by_away[0]["game_id"] == match_id:
        actual_match_stats_by_away = filtered_stats_by_away[0]
        filtered_stats_by_away.pop(0)

    if "vs" in actual_match_stats_by_home["matchup"]:
        actual_stats = calculate_stats(actual_match_stats_by_home, actual_match_stats_by_away["pts"])
    else:
        actual_stats = calculate_stats(actual_match_stats_by_away, actual_match_stats_by_home["pts"])

    final_stats = []
    for stat_home in filtered_stats_by_home:
        for stat_away in filtered_stats_by_away:
            if stat_away["game_id"] == stat_home["game_id"]:
                if "vs" in stat_home["matchup"]:
                    final_stats.append(calculate_stats(stat_home, stat_away["pts"]))
                else:
                    final_stats.append(calculate_stats(stat_away, stat_home["pts"]))

    return {"actual_match_stats": {"global_stats": actual_stats,
                                   "by_home_stats": actual_match_stats_by_home,
                                   "by_away_stats": actual_match_stats_by_away},
            "last_match_stats": {"global_stats": final_stats,
                                 "by_home_stats": filtered_stats_by_home,
                                 "by_away_stats": filtered_stats_by_away}}
