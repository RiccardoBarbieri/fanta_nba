import { Injectable } from '@angular/core';
import {Standings} from "./standings";

@Injectable({
  providedIn: 'root'
})
export class StandingsService {
  nba_api_url = "https://nba-api.orangewave-05a306f8.westeurope.azurecontainerapps.io";

  async getStandingsForDate(date: string): Promise<Standings> {
    const data = await fetch(this.nba_api_url + '/standings?' + new URLSearchParams({
      date: date
    }), {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? {};
  }
}
