import {Component, inject} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Title} from "@angular/platform-browser";
import {Team} from "../team";
import {TeamsService} from "../teams.service";
import {CardModule} from "primeng/card";
import {CarouselModule} from "primeng/carousel";
import {DataViewModule} from "primeng/dataview";
import {MatchListComponent} from "../match-list/match-list.component";
import {Match} from "../match";
import {MatchesService} from "../matches.service";
import {getFormattedDate} from "../../shared/utils";
import {ScrollPanelModule} from "primeng/scrollpanel";
import {DividerModule} from "primeng/divider";
import {CalendarModule} from "primeng/calendar";
import {FormsModule} from "@angular/forms";
import {PlayerShowcaseComponent} from "./player-showcase/player-showcase.component";
import {TimeTravelComponent} from "../../shared/time-travel/time-travel.component";
import {TimeTravelService} from "../../shared/time-travel.service";

@Component({
  selector: 'app-team-details',
  standalone: true,
  imports: [
    CardModule,
    CarouselModule,
    DataViewModule,
    MatchListComponent,
    ScrollPanelModule,
    DividerModule,
    CalendarModule,
    FormsModule,
    PlayerShowcaseComponent,
    TimeTravelComponent
  ],
  templateUrl: './team-details.component.html',
  styleUrl: './team-details.component.css'
})
export class TeamDetailsComponent {
  timetravelService = inject(TimeTravelService);
  route: ActivatedRoute = inject(ActivatedRoute);
  teamsService = inject(TeamsService);
  matchesService = inject(MatchesService);
  team: Team | undefined;
  matches: Match[] = [] ;

  date: Date;
  next_week = () => {
    return new Date(this.date.getFullYear(), this.date.getMonth(), this.date.getDate() + 7)
  };

  constructor(private titleService: Title) {
    this.date = this.timetravelService.date;
    this.titleService.setTitle('Team Details');
    const ticker = this.route.snapshot.params["ticker"];
    this.teamsService.getTeamFromTicker(ticker, "2023-24").then((team: Team) => {
      this.team = team;
      this.matchesService.getMatchesByDate(getFormattedDate(this.date),getFormattedDate(this.next_week())).then((matches: Match[]) => {
        this.matches = matches.filter((match: Match) => {return match.home_team.id === team.team_info.id || match.away_team.id === team.team_info.id});
      })
    });
  }

  refreshMatches() {
    this.date = this.timetravelService.date;
    this.matches = [];
    // this.loading = true;
    this.matchesService.getMatchesByDate(getFormattedDate(this.date),
      getFormattedDate(this.next_week())).then((matches: Match[]) => {
      this.matches = matches;
      // this.loading = false;
    })
  }
}
