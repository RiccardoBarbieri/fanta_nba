import {TeamInfo} from "./team";
import {Referee} from "./referee";

export interface Match {
  game_id: number,
  match_up: string,
  date: string, // maybe use Date?
  home_team: TeamInfo,
  away_team: TeamInfo,
  referee: Referee,
}
