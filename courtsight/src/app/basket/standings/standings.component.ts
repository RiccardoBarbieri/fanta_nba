import { Component } from '@angular/core';
import {TableModule} from "primeng/table";
import {CardModule} from "primeng/card";
import {Button, ButtonDirective} from "primeng/button";
import {DatePipe} from "@angular/common";
import {RouterLink} from "@angular/router";
import {StandingsListComponent} from "./standings-list/standings-list.component";

@Component({
  selector: 'app-standings',
  standalone: true,
  imports: [
    TableModule,
    CardModule,
    Button,
    DatePipe,
    RouterLink,
    ButtonDirective,
    StandingsListComponent,
  ],
  templateUrl: './standings.component.html',
  styleUrl: './standings.component.css'
})
export class StandingsComponent {
  last_update!: Date;

  constructor() {
    this.last_update = new Date();
  }

  refreshStandings() {
    this.last_update = new Date();
  }

  openTeamDetails() {
  }

  teams : Row[] = [
    {
      team_id: 1,
      ticker: "BOS",
      name: "Boston Celtics",
      w: 64,
      l: 18,
    },
    {
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },
    {
      team_id: 3,
      ticker: "MBS",
      name: "Milwaukee Bucks",
      w: 49,
      l: 33,
    },
    {
      team_id: 4,
      ticker: "LOL",
      name: "Cleveland Cavaliers",
      w: 48,
      l: 34,
    },
    {
      team_id: 5,
      ticker: "OMA",
      name: "Orlando Magic",
      w: 47,
      l: 35,
    },
    {
      team_id: 5,
      ticker: "OMA",
      name: "Orlando Magic",
      w: 47,
      l: 35,
    },
    {
      team_id: 5,
      ticker: "OMA",
      name: "Orlando Magic",
      w: 47,
      l: 35,
    },
    {
      team_id: 5,
      ticker: "OMA",
      name: "Orlando Magic",
      w: 47,
      l: 35,
    },
    {
      team_id: 5,
      ticker: "OMA",
      name: "Orlando Magic",
      w: 47,
      l: 35,
    },
    {
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },
    {
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },{
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },
    {
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },
    {
      team_id: 2,
      ticker: "CFR",
      name: "New York Knicks",
      w: 50,
      l: 32,
    },


  ]
}

export interface Row { // TODO change
  team_id: number,
  ticker: string,
  name: string,
  w: number,
  l: number,
}
