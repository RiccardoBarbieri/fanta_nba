import {Component, Input, OnInit} from '@angular/core';
import {TeamMatchStats} from "../../stats";
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
  @Input() alignment: "left" | "right" = "left";
  @Input() stats!: TeamMatchStats;

  rows: Row[] = [];

  ngOnInit() {
    this.rows = [
      {
        name: "Assist",
        value: this.stats.ast
      },
      {
        name: "Turnovers",
        value: this.stats.tov
      },
      {
        name: "Field Goal Percentage",
        value: this.stats.fg_pct
      },
      {
        name: "Assist",
        value: this.stats.ast
      },
      {
        name: "Turnovers",
        value: this.stats.tov
      },
      {
        name: "Field Goal Percentage",
        value: this.stats.fg_pct
      },
    ]
  }

}
