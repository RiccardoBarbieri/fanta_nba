import {Component, inject, OnInit} from '@angular/core';
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
    FormsModule
  ],
  templateUrl: './team-details.component.html',
  styleUrl: './team-details.component.css'
})
export class TeamDetailsComponent implements OnInit {
  route: ActivatedRoute = inject(ActivatedRoute);
  teamsService = inject(TeamsService);
  matchesService = inject(MatchesService);
  team: Team | undefined;
  matches: Match[] = [] ;

  date: Date = new Date("2023-11-05");
  current_date: Date;
  next_week = () => {
    return new Date(this.current_date.getFullYear(), this.current_date.getMonth(), this.current_date.getDate() + 7)
  };

  // today: Date = new Date("2023-11-05");
  // next_week: Date = new Date(this.today.getFullYear(), this.today.getMonth(), this.today.getDate()+7);

  responsiveOptions: any[] | undefined;

  constructor(private titleService: Title) {
    this.current_date = this.date;
    this.titleService.setTitle('Team Details');
    const ticker = this.route.snapshot.params["ticker"];
    // this.team = mockTeam; // TODO debug
    // this.matches = mockMatches;
    this.teamsService.getTeamFromTicker(ticker, "2023-24").then((team: Team) => {
      this.team = team;
      this.matchesService.getMatchesByDate(getFormattedDate(this.current_date),getFormattedDate(this.next_week())).then((matches: Match[]) => {
        this.matches = matches.filter((match: Match) => {return match.home_team.id === team.team_info.id || match.away_team.id === team.team_info.id});
      })
    });
  }

  refreshMatches() {
    this.current_date = this.date;
    this.matches = [];
    // this.loading = true;
    this.matchesService.getMatchesByDate(getFormattedDate(this.current_date),
      getFormattedDate(this.next_week())).then((matches: Match[]) => {
      this.matches = matches;
      // this.loading =false;
    })
  }

  ngOnInit(): void {
    this.responsiveOptions = [
      {
        breakpoint: '1500px',
        numVisible: 4,
        numScroll: 4
      },
      {
        breakpoint: '1000px',
        numVisible: 3,
        numScroll: 3
      },
      {
        breakpoint: '500px',
        numVisible: 1,
        numScroll: 1
      }
    ];
  }
}
