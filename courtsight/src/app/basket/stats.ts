export interface GlobalStats {
  game_id: string,
  game_date: string,
  match_up: string,
  winner: string,
  home_point: number,
  away_point: number,
}

export interface TeamMatchStats {
  season_id: string
  team_id: number,
  team_abbreviation: string,
  team_name: string,
  game_id: string,
  game_date: string,
  match_up: string,
  wl: string,
  min: number,
  fgm: number,
  fga: number,
  fg_pct: number,
  fg3m: number,
  fg3a: number,
  fg3_pct: number,
  ftm: number,
  fta: number,
  ft_pct: number,
  oreb: number,
  dreb: number,
  reb: number,
  ast: number,
  stl: number,
  blk: number,
  tov: number,
  pf: number,
  pts: number,
  plus_minus: number,
  video_available: number,
}

export interface PlayerMatchStats {
  season_id: number,
  player_id: number,
  game_id: string,
  game_date: string,
  match_up: string,
  wl: string,
  min: number,
  fgm: number,
  fga: number,
  fg_pct: number,
  fg3m: number,
  fg3a: number,
  fg3_pct: number,
  ftm: number,
  fta: number,
  ft_pct: number,
  oreb: number,
  dreb: number,
  reb: number,
  ast: number,
  stl: number,
  blk: number,
  tov: number,
  pf: number,
  pts: number,
  plus_minus: number,
  video_available: number,
}

export interface MatchStats {
  global_stats: GlobalStats,
  by_home_stats: TeamMatchStats,
  by_away_stats: TeamMatchStats,
}

export interface ActualAndLastMatchStats {
  actual_match_stats: MatchStats
  last_match_stats: MatchStats,
}

export interface TeamStats {
  all_stats: TeamMatchStats[],
  totals: {},
  average: {}
}

export interface PlayerStats {
  all_stats: PlayerMatchStats[],
  totals: {},
  average: {}
}
