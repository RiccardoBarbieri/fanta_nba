import {Injectable} from '@angular/core';
import {Odds} from "./odds";

@Injectable({
  providedIn: 'root'
})
export class OddsService {
  bet_api_url: string = "https://bet-api.orangewave-05a306f8.westeurope.azurecontainerapps.io";

  async getOddsForMatch(eventId: string, sportKey: string = "basketball_nba", regions: string = "eu"): Promise<Odds[]> {
    const params = new URLSearchParams(
      {
        eventId: eventId,
        sportKey: sportKey,
        regions: regions,
      });

    const data = await fetch(`${this.bet_api_url}/odds/head2head?${params.toString()}`, {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? [];
  }
}
