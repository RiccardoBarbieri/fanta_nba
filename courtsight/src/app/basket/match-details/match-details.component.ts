import {Component, inject} from '@angular/core';
import {ActivatedRoute, RouterLink} from "@angular/router";
import {MatchesService} from "../matches.service";
import {Match} from "../match";
import {DividerModule} from "primeng/divider";
import {ActualAndLastMatchStats, MatchStats} from "../stats";
import {FieldsetModule} from "primeng/fieldset";
import {CommonModule, DatePipe} from "@angular/common";
import {SplitterModule} from "primeng/splitter";
import {StatsTableComponent} from "./stats-table/stats-table.component";
import {MeterGroupModule, MeterItem} from "primeng/metergroup";
import {PanelModule} from "primeng/panel";
import {CardModule} from "primeng/card";

@Component({
  selector: 'app-match-details',
  standalone: true,
  imports: [
    DividerModule,
    RouterLink,
    FieldsetModule,
    DatePipe,
    SplitterModule,
    StatsTableComponent,
    MeterGroupModule,
    CommonModule,
    PanelModule,
    CardModule
  ],
  templateUrl: './match-details.component.html',
  styleUrl: './match-details.component.css'
})
export class MatchDetailsComponent {
  route: ActivatedRoute = inject(ActivatedRoute);
  matchesService = inject(MatchesService);

  matchStats: MatchStats | undefined;
  meterValue: MeterItem[] = [];

  constructor() {
    const match_id = this.route.snapshot.params["id"];
    const match_date = this.route.snapshot.params["date"];

    this.matchesService.getMatchStatsById(match_id, match_date).then((matches: ActualAndLastMatchStats) => {
      this.matchStats = matches.actual_match_stats

      let homePts = this.matchStats.by_home_stats.pts;
      let awayPts = this.matchStats.by_away_stats.pts;
      let total = homePts + awayPts;

      this.meterValue = [
        {label: '', value: homePts / total * 100, color: homePts >= awayPts ? colors.winningLeft : colors.losingLeft},
        {label: '', value: awayPts / total * 100, color: homePts < awayPts ? colors.winningRight : colors.losingRight},
      ]

    });
    // this.matchStats = mochMatchStats.actual_match_stats;
  }
}

export const colors = {
  winningLeft: "#3bc21d",
  losingLeft: "rgba(73,225,11,0.25)",
  winningRight: "#eb9c08",
  losingRight: "rgba(235,156,8,0.25)",
}

const mockMatch: Match =
  {
    "game_id": 12345,
    "match_up": "BKN - WAS",
    "date": "JUL 12, 2024",
    "home_team": {
      "id": 1610612767,
      "full_name": "Washington Wizards",
      "abbreviation": "WAS",
      "nickname": "Wizards",
      "city": "Washington",
      "state": "DC",
      "year_founded": 1939,
      "arena": "Nome a caso Arena"
    },
    "away_team": {
      "id": 1610612738,
      "full_name": "Boston Celtics",
      "abbreviation": "BOS",
      "nickname": "Celtics",
      "city": "Boston",
      "state": "MA",
      "year_founded": 1946,
      "arena": "Nome a caso Arena"
    },
    "referee": {
      "name": "Sean Corbin",
      "id": 1151
    },
    "arena": {
      "name": "Capital One Arena",
      "city": "Washington",
      "state": "DC",
      "country": "US"
    }
  }
const mochMatchStats: ActualAndLastMatchStats = {
  actual_match_stats:
    {
      global_stats: {
        game_id: "0022301198",
        game_date: "2024-04-14",
        match_up: "GSW vs. UTA",
        winner: "GSW",
        home_point: 123,
        away_point: 116
      },
      by_home_stats: {
        season_id: "22023",
        team_id: 1610612738,
        team_abbreviation: "BOS",
        team_name: "Boston Celtics",
        game_id: "0022001074",
        game_date: "2024-01-23",
        match_up: "BOS vs. LAL",
        wl: "W",
        min: 240,
        fgm: 40,
        fga: 85,
        fg_pct: 47.1,
        fg3m: 12,
        fg3a: 32,
        fg3_pct: 37.5,
        ftm: 18,
        fta: 22,
        ft_pct: 81.8,
        oreb: 10,
        dreb: 35,
        reb: 45,
        ast: 25,
        stl: 8,
        blk: 5,
        tov: 13,
        pf: 20,
        pts: 110,
        plus_minus: -6,
        video_available: 1
      },
      by_away_stats: {
        season_id: "22023",
        team_id: 1610612738,
        team_abbreviation: "BOS",
        team_name: "Boston Celtics",
        game_id: "0022001074",
        game_date: "2024-01-23",
        match_up: "BOS vs. LAL",
        wl: "W",
        min: 240,
        fgm: 40,
        fga: 85,
        fg_pct: 47.1,
        fg3m: 12,
        fg3a: 32,
        fg3_pct: 37.5,
        ftm: 18,
        fta: 22,
        ft_pct: 81.8,
        oreb: 10,
        dreb: 35,
        reb: 45,
        ast: 25,
        stl: 8,
        blk: 5,
        tov: 13,
        pf: 20,
        pts: 131,
        plus_minus: -6,
        video_available: 1
      }
    },
  last_match_stats: {
    global_stats: {
      game_id: "0022301198",
      game_date: "2024-04-14",
      match_up: "GSW vs. UTA",
      winner: "GSW",
      home_point: 123,
      away_point: 116
    },
    by_home_stats:
      {
        season_id: "22023",
        team_id: 1610612738,
        team_abbreviation: "BOS",
        team_name: "Boston Celtics",
        game_id: "0022001074",
        game_date: "2024-01-23",
        match_up: "BOS vs. LAL",
        wl: "W",
        min: 240,
        fgm: 40,
        fga: 85,
        fg_pct: 47.1,
        fg3m: 12,
        fg3a: 32,
        fg3_pct: 37.5,
        ftm: 18,
        fta: 22,
        ft_pct: 81.8,
        oreb: 10,
        dreb: 35,
        reb: 45,
        ast: 25,
        stl: 8,
        blk: 5,
        tov: 13,
        pf: 20,
        pts: 110,
        plus_minus: -6,
        video_available: 1
      },
    by_away_stats:
      {
        season_id: "22023",
        team_id: 1610612738,
        team_abbreviation: "BOS",
        team_name: "Boston Celtics",
        game_id: "0022001074",
        game_date: "2024-01-23",
        match_up: "BOS vs. LAL",
        wl: "W",
        min: 240,
        fgm: 40,
        fga: 85,
        fg_pct: 47.1,
        fg3m: 12,
        fg3a: 32,
        fg3_pct: 37.5,
        ftm: 18,
        fta: 22,
        ft_pct: 81.8,
        oreb: 10,
        dreb: 35,
        reb: 45,
        ast: 25,
        stl: 8,
        blk: 5,
        tov: 13,
        pf: 20,
        pts: 110,
        plus_minus: -6,
        video_available: 1
      }
  }
}
