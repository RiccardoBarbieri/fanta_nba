import {Component, inject} from '@angular/core';
import {StandingsComponent} from "../standings/standings.component";
import {CardModule} from "primeng/card";
import {CommonModule, DatePipe} from "@angular/common";
import {DividerModule} from "primeng/divider";
import {Match} from "../match";
import {DataViewModule} from "primeng/dataview";
import {TagModule} from "primeng/tag";
import {RouterLink} from "@angular/router";
import {Button} from "primeng/button";
import {MatchListComponent} from "../match-list/match-list.component";
import {MatchesService} from "../matches.service";
import {counterArray, getFormattedDate} from "../../shared/utils";
import {CalendarModule} from "primeng/calendar";
import {FormsModule} from "@angular/forms";
import {InputGroupModule} from "primeng/inputgroup";
import {SkeletonModule} from "primeng/skeleton";
import {TimeTravelComponent} from "../../shared/time-travel/time-travel.component";
import {TimeTravelService} from "../../shared/time-travel.service";


@Component({
  selector: 'app-basket-home',
  standalone: true,
  imports: [
    StandingsComponent,
    CardModule,
    DatePipe,
    DividerModule,
    DataViewModule,
    TagModule,
    CommonModule,
    RouterLink,
    Button,
    MatchListComponent,
    CalendarModule,
    FormsModule,
    InputGroupModule,
    SkeletonModule,
    TimeTravelComponent,
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  timetravelService = inject(TimeTravelService);
  matchesService = inject(MatchesService);
  date: Date;
  next_week = () => {
    return new Date(this.date.getFullYear(), this.date.getMonth(), this.date.getDate() + 7)
  };
  matches: Match[] = [];
  loading = false;

  constructor() {
    this.date = this.timetravelService.date;
    this.refreshMatches();
  }

  refreshMatches() {
    this.date = this.timetravelService.date;
    this.matches = [];
    this.loading = true;
    this.matchesService.getMatchesByDate(getFormattedDate(this.date),
      getFormattedDate(this.next_week())).then((matches: Match[]) => {
      this.matches = matches;
      this.loading =false;
    })
  }

  protected readonly counterArray = counterArray;
}
