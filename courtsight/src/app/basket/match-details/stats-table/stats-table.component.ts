import {Component, Input, OnInit} from '@angular/core';
import {MatchStats, TeamMatchStats} from "../../stats";
import {Row, StatsRowComponent} from "./stats-row/stats-row.component";
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-stats-table',
  standalone: true,
  imports: [
    StatsRowComponent,
    CommonModule
  ],
  templateUrl: './stats-table.component.html',
  styleUrl: './stats-table.component.css'
})
export class StatsTableComponent implements OnInit {
  @Input() stats!: MatchStats;

  rows: Row[] = [];

  ngOnInit() {
    const home: TeamMatchStats = this.stats.by_home_stats;
    const away: TeamMatchStats = this.stats.by_away_stats;

    this.rows = [
      // {name: "Points", leftValue: home.pts, rightValue: away.pts,},
      {name: "Field Goals Made", leftValue: home.fgm, rightValue: away.fgm,},
      {name: "Field Goals Attempted", leftValue: home.fga, rightValue: away.fga,},
      {name: "Field Goal Percentage", leftValue: home.fg_pct, rightValue: away.fg_pct,},
      {name: "Three-Point Field Goals Made", leftValue: home.fg3m, rightValue: away.fg3m,},
      {name: "Three-Point Field Goals Attempted", leftValue: home.fg3a, rightValue: away.fg3a,},
      {name: "Three-Point Field Goal Percentage", leftValue: home.fg3_pct, rightValue: away.fg3_pct,},
      {name: "Free Throws Made", leftValue: home.ftm, rightValue: away.ftm,},
      {name: "Free Throws Attempted", leftValue: home.fta, rightValue: away.fta,},
      {name: "Free Throw Percentage", leftValue: home.ft_pct, rightValue: away.ft_pct,},
      {name: "Offensive Rebounds", leftValue: home.oreb, rightValue: away.oreb,},
      {name: "Defensive Rebounds", leftValue: home.dreb, rightValue: away.dreb,},
      {name: "Total Rebounds", leftValue: home.reb, rightValue: away.reb,},
      {name: "Assists", leftValue: home.ast, rightValue: away.ast,},
      {name: "Steals", leftValue: home.stl, rightValue: away.stl,},
      {name: "Blocks", leftValue: home.blk, rightValue: away.blk,},
      {name: "Turnovers", leftValue: home.tov, rightValue: away.tov,},
      {name: "Personal Fouls", leftValue: home.pf, rightValue: away.pf,},
      // {name: "Minutes Played", leftValue: home.min, rightValue: away.min,},
      // {name: "Plus/Minus", leftValue: home.plus_minus, rightValue: away.plus_minus,},
    ]
  }
}
