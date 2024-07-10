import featurevec.feature_vector_helper as feature_vector_helper
import featurevec.rest_api_functions_helper as helper

# Rest Api Controller for player information and statistics


def get_player_stats(player_id: str, season: str, date_to: str, last_x: int | None, home_away_filter: str | None) -> (
        dict)[str, list[dict]]:
    """
    Retrieve team statistics based on provided parameters.

    :param player_id: The Player identifier.
    :param season: The season in the format 'YYYY-YY'.
    :param date_to: The cutoff date until which games are considered.
    :param last_x: Optional filter for the number of recent games to consider.
    :param home_away_filter: Optional filter for home ('HOME') or away ('AWAY') games.
    :return: A dictionary containing filtered game statistics, total wins and losses, and averages.
    """

    all_stats = helper.get_all_player_games_until_date_to(player_id, season, date_to)
    filtered_stats = helper.get_last_games_at_home_away(all_stats, last_x, home_away_filter)

    total_wins, total_losses, averages = helper.calculate_sums_averages(filtered_stats)
    filtered_player_efficiency = helper.get_filtered_matches_player_efficiency(filtered_stats)

    game_id_up_to = filtered_stats.__getitem__(0).get("game_id")
    player_efficiency = feature_vector_helper.get_player_efficiency(player_id, game_id_up_to, season)

    return {
        "all_stats": filtered_stats,
        "totals": {"wins": total_wins, "losses": total_losses},
        "average": averages,
        "player_efficiency": {"all": player_efficiency, "filtered_matches": filtered_player_efficiency}
    }