import {Injectable} from '@angular/core';
import {Match} from "./match";
import {ActualAndLastMatchStats} from "./stats";

@Injectable({
  providedIn: 'root'
})
export class MatchesService {
  nba_api_url = "http://localhost:8080/api/";

  constructor() {
  }

  // async getMatches(match_up: string, season: string, matchday: string): Promise<Match[]> {
  //   const data = await fetch(this.nba_api_url + 'matches' +
  //     new URLSearchParams({
  //       match_up: match_up,
  //       season: season,
  //       matchday: matchday,
  //     }).toString()
  //   );
  //   return await data.json() ?? [];
  // }

  // async getMatchById(game_id: number): Promise<Match> {
  //   const data = await fetch(this.nba_api_url + 'match/' + game_id);
  //   return await data.json() ?? {};
  // }
  //
  // async getMatch(match_up: string, season: string, matchday: string): Promise<Match> {
  //   const data = await fetch(this.nba_api_url + 'match/' + new URLSearchParams({
  //     match_up: match_up,
  //     season: season,
  //     matchday: matchday,
  //   }).toString());
  //   return await data.json() ?? {};
  // }

  async getMatchesByDate(date_from: string, date_to: string | undefined): Promise<Match[]> {
    const params = new URLSearchParams(
      {
        date_from: date_from,
      });
    if (date_to) {
      params.append('date_to', date_to);
    }
    const data = await fetch(this.nba_api_url + 'matches' + params.toString());
    return await data.json() ?? [];
  }

  async getMatchStatsById(match_id: number, match_date: string): Promise<ActualAndLastMatchStats[]> {
    const data = await fetch(this.nba_api_url + 'match/' + match_id + '/stats' + new URLSearchParams({
      match_date: match_date,
    }));
    return await data.json() ?? {};
  }
}
