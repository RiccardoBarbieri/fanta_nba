import {Injectable} from '@angular/core';
import {Match} from "./match";
import {ActualAndLastMatchStats} from "./stats";
import {Vector} from "./vector";

@Injectable({
  providedIn: 'root'
})
export class MatchesService {
  nba_api_url = "https://nba-api.orangewave-05a306f8.westeurope.azurecontainerapps.io";

  async getFeatureVectorForMatch(team_ticker: string, opp_ticker: string, season: string, date: string): Promise<Vector> {
    const data = await fetch(this.nba_api_url + '/feature_vector?' + new URLSearchParams({
      team_ticker: team_ticker,
      opp_team_ticker: opp_ticker,
      season: season,
      date: date
    }), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? {};
  }

  async getMatchesByDate(date_from: string, date_to: string | undefined): Promise<Match[]> {
    const params = new URLSearchParams(
      {
        date_from: date_from,
      });
    if (date_to) {
      params.append('date_to', date_to);
    }
    const data = await fetch(this.nba_api_url + '/matches?' + params.toString(), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? [];
  }

  async getMatchStatsById(match_id: number, match_date: string): Promise<ActualAndLastMatchStats> {
    const data = await fetch(`${this.nba_api_url}/match/${match_id}/stats?` + new URLSearchParams({
      match_date: match_date,
    }), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? {};
  }
}
