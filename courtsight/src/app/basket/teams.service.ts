import {Injectable} from '@angular/core';
import {Team} from "./team";
import {TeamStats} from "./stats";

@Injectable({
  providedIn: 'root'
})
export class TeamsService {
  nba_api_url = "https://nba-api.orangewave-05a306f8.westeurope.azurecontainerapps.io/teams";

  constructor() {
  }

  async getTeams(team_tickers: string[], season: string): Promise<Team[]> {
    const params = new URLSearchParams({season: season});
    for (const ticker of team_tickers) {
      params.append('team_tickers', ticker);
    }

    const data = await fetch(this.nba_api_url + params.toString(), {
        headers: {
          "Accept": "application/json",
        }
      }
    );
    return await data.json() ?? [];
  }

  async getTeamFromTicker(team_ticker: string, season: string): Promise<Team> {
    const data = await fetch(`${this.nba_api_url}/${team_ticker}?` + new URLSearchParams({season: season}).toString(), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? {};
  }

  async getTeamStatsById(team_id: number, season: string, date_to: string, last_x: string | undefined, home_away_filter: string | undefined): Promise<TeamStats> {
    const params = new URLSearchParams(
      {
        season: season,
        date_to: date_to,
      });
    if (last_x) {
      params.append('last_x', last_x);
    }
    if (home_away_filter) {
      params.append('location', home_away_filter);
    }

    const data = await fetch(`${this.nba_api_url}/${team_id}/stats?` + params.toString(), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? {};
  }
}
