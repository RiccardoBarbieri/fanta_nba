import {Player} from "./player";

export interface TeamInfo {
  id: number,
  full_name: string,
  abbreviation: string,
  nickname: string,
  city: string,
  state: string,
  year_founded: number,
  arena: string,
}

export interface Team {
  team_ticker: string,
  team_info: TeamInfo,
  team_players: Player[]
}
