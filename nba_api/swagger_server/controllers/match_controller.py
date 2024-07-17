import datetime
import featurevec.feature_vector_helper as feature_vector_helper
import featurevec.rest_api_functions_helper as helper


# Rest Api Controller for match information and statistics

def match_match_id_stats_get(match_id: str, match_date: str) -> dict[str, any]:
    """
    Retrieve match statistics for a specific match.

    :param match_id: The ID of the match.
    :param match_date: The date of the match in the format 'YYYY-MM-DD'.
    :return: Dictionary containing actual and last match statistics.
    """

    matches = helper.get_league_game_log_by_date(match_date, match_date)
    actual_matches = list(filter(lambda matches: matches['game_id'] == match_id, matches))

    date_from = datetime.datetime.strptime(match_date, '%Y-%m-%d')
    date_from = date_from.replace(year=date_from.year - 1).strftime('%m/%d/%Y')
    date_to = datetime.datetime.strptime(match_date, '%Y-%m-%d').strftime('%m/%d/%Y')

    direct_matchups = helper.get_direct_matchups(actual_matches.__getitem__(0)["team_id"],
                                                 actual_matches.__getitem__(1)["team_id"],
                                                 date_from, date_to) + helper.get_direct_matchups(
        actual_matches.__getitem__(1)["team_id"],
        actual_matches.__getitem__(0)["team_id"],
        date_from, date_to)

    if "vs" in actual_matches.__getitem__(0)["matchup"]:
        actual_stats = helper.calculate_stats(actual_matches.__getitem__(0), actual_matches.__getitem__(1)["pts"])
    else:
        actual_stats = helper.calculate_stats(actual_matches.__getitem__(1), actual_matches.__getitem__(0)["pts"])

    final_stats = []
    half_index = int(len(direct_matchups) / 2)
    for i in range(0, half_index, 1):
        stats_0 = direct_matchups.__getitem__(i)
        stats_1 = direct_matchups.__getitem__(i + half_index)
        if stats_0["game_id"] == match_id:
            continue
        if "vs" in stats_0["matchup"]:
            final_stats.append(helper.calculate_stats(stats_0, stats_1["pts"]))
        else:
            final_stats.append(helper.calculate_stats(stats_1, stats_0["pts"]))

    return {"actual_match_stats": {"global_stats": actual_stats,
                                   "by_home_stats": actual_matches.__getitem__(1),
                                   "by_away_stats": actual_matches.__getitem__(0)},
            "last_match_stats": {"global_stats": final_stats,
                                 "by_home_stats": list(filter(lambda direct_matchups:
                                                              actual_matches.__getitem__(1)["team_abbreviation"] ==
                                                              direct_matchups["team_abbreviation"] and direct_matchups[
                                                                  "game_id"] != match_id, direct_matchups)),
                                 "by_away_stats": list(filter(lambda direct_matchups:
                                                              actual_matches.__getitem__(0)["team_abbreviation"] ==
                                                              direct_matchups["team_abbreviation"] and direct_matchups[
                                                                  "game_id"] != match_id, direct_matchups))}}


def matches_get(date_from: str, date_to: str | None = None) -> list[dict[str, str]]:
    if date_to is None:
        date_to = date_from

    matches = helper.get_league_game_log_by_date(date_from, date_to)

    res = []
    if matches is None:
        return res

    for match in matches:
        if "@" in match["matchup"]:
            continue

        game_id = match["game_id"]
        home_team = helper.get_team_info_by_ticker(match["team_abbreviation"])
        away_team = helper.get_team_info_by_ticker(match["matchup"][-3:])

        referee = feature_vector_helper.get_referee(game_id)

        res.append(
            {"match_up": match["matchup"], "game_id": game_id, "date": match["game_date"], "home_team": home_team,
             "away_team": away_team, "referee": referee})

    return res
