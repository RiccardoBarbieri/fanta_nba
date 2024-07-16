export interface TeamStandings {
  team_id: number,
  league_id: string,
  season_id: string,
  standingsdate: string,
  conference: string,
  team: string,
  team_ticker: string,
  g: number,
  w: number,
  l: number,
  w_pct: number,
  home_record: string,
  road_record: string,
}

export interface Standings {
  west: TeamStandings[],
  east: TeamStandings[],
}
