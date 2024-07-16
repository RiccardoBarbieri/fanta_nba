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
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  matchesService = inject(MatchesService);
  date: Date = new Date("2023-11-05");
  current_date: Date;
  next_week = () => {
    return new Date(this.current_date.getFullYear(), this.current_date.getMonth(), this.current_date.getDate() + 7)
  };
  matches: Match[] = [];
  loading = false;

  constructor() {
    this.current_date = this.date;
    this.refreshMatches();
  }

  refreshMatches() {
    this.current_date = this.date;
    this.matches = [];
    this.loading = true;
    this.matchesService.getMatchesByDate(getFormattedDate(this.current_date),
      getFormattedDate(this.next_week())).then((matches: Match[]) => {
      this.matches = matches;
      this.loading =false;
    })
  }

  protected readonly counterArray = counterArray;
}
