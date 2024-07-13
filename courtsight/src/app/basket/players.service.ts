import { Injectable } from '@angular/core';
import {PlayerStats} from "./stats";

@Injectable({
  providedIn: 'root'
})
export class PlayersService {
  nba_api_url = "http://localhost:8080/api/players";

  constructor() { }

  async getPlayerStatsById(player_id: number, season: string, date_to: string | undefined, last_x: string | undefined, home_away_filter: string | undefined): Promise<PlayerStats> {
    const params = new URLSearchParams(
      {
        season: season,
      })
    if (date_to) {
      params.append('date_to', date_to);
    }
    if (last_x) {
      params.append('last_x', last_x);
    }
    if (home_away_filter) {
      params.append('home_away_filter', home_away_filter);
    }

    const data = await fetch(`${this.nba_api_url}/${player_id}/stats` + params.toString());
    return await data.json() ?? {};
  }
}
