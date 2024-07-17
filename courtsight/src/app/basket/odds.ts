export interface Event {
  id: string,
  sport_key: string,
  sport_title: string,
  commence_time: string,
  home_team: string,
  away_team: string,
}

export interface Bookmaker {
  url: string,
  key: string,
  title: string,
  last_update: string,
  markets: Market[],
}

export interface Market {
  key: "h2h" | "spreads" | "totals" | "outrights",
  last_update: string,
  outcomes: Outcome[]
}

export interface Outcome {
  name: string,
  price: number,
  point: number,
  description: string,
}

export interface Odds {
  event: Event,
  bookmakers: Bookmaker[],
}
