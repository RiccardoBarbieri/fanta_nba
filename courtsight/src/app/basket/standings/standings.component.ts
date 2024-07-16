import {Component, inject} from '@angular/core';
import {TableModule} from "primeng/table";
import {CardModule} from "primeng/card";
import {Button, ButtonDirective} from "primeng/button";
import {DatePipe} from "@angular/common";
import {RouterLink} from "@angular/router";
import {StandingsListComponent} from "./standings-list/standings-list.component";
import {BadgeModule} from "primeng/badge";
import {AvatarModule} from "primeng/avatar";
import {StandingsService} from "../standings.service";
import {getFormattedDate} from "../../shared/utils";
import {Standings} from "../standings";

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
    BadgeModule,
    AvatarModule,
  ],
  templateUrl: './standings.component.html',
  styleUrl: './standings.component.css'
})
export class StandingsComponent {
  standingsService = inject(StandingsService);
  last_update!: Date;

  standings : Standings | undefined;

  constructor() {
    this.refreshStandings()
  }

  refreshStandings() {
    this.last_update = new Date();
    this.standingsService.getStandingsForDate(getFormattedDate(this.last_update)).then((standings: Standings) => {
      this.standings = standings;
    })
  }
}

