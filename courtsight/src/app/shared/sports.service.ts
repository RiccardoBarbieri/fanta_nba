import {Injectable} from '@angular/core';
import {AvailableSport} from './sport';
import {Sport} from "../sport";

@Injectable({
  providedIn: 'root'
})
export class SportsService {
  bet_api_url: string = "https://bet-api.orangewave-05a306f8.westeurope.azurecontainerapps.io";

  constructor() {}

  async getAllSports(): Promise<Sport[]> {
    const data = await fetch(`${this.bet_api_url}/sports/getSports`, {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? [];
  }

  async getSportGroups(): Promise<string[]> {
    const data = await fetch(`${this.bet_api_url}/sports/getSportGroups`, {
      headers: {
        "Accept": "application/json",
      }
    });
    return await data.json() ?? [];
  }

  async getAvailableSports(): Promise<AvailableSport[]> {
    const all_sports = await this.getSportGroups();
    const available_sports: AvailableSport[] = [{
      name: "Basketball",
      features: [
        {
          name: "Match predictions",
          available: true,
        },
        {
          name: "Bookmakers Integration",
          available: true,
        },
      ],
      url: '/basketball'
    }];

    for (let sport of all_sports) {
      if (sport != "Basketball") {
        available_sports.push(
          {
            name: sport,
            features: [
              {
                name: "Match predictions",
                available: false,
              },
              {
                name: "Bookmakers Integration",
                available: true,
              },
            ],
            url: undefined
          });
      }
    }

    return available_sports;
  }
}
