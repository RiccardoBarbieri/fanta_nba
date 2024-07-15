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

@Component({
  selector: 'app-team-details',
  standalone: true,
  imports: [
    CardModule,
    CarouselModule,
    DataViewModule,
    MatchListComponent
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
  today: Date = new Date("2023-10-14");
  next_week: Date = new Date(this.today.getFullYear(), this.today.getMonth(), this.today.getDate()+7);

  responsiveOptions: any[] | undefined;

  constructor(private titleService: Title) {
    this.titleService.setTitle('Team Details');
    const ticker = this.route.snapshot.params["ticker"];
    // this.team = mockTeam; // TODO debug
    // this.matches = mockMatches;
    this.teamsService.getTeamFromTicker(ticker, "2023-24").then((team: Team) => {
      this.team = team;
      this.matchesService.getMatchesByDate(getFormattedDate(this.today),getFormattedDate(this.next_week)).then((matches: Match[]) => {
        this.matches = matches.filter((match: Match) => {return match.home_team.id === team.team_info.id || match.away_team.id === team.team_info.id});
      })
    });
  }

  ngOnInit(): void {
    this.responsiveOptions = [
      {
        breakpoint: '1199px',
        numVisible: 5,
        numScroll: 1
      },
      {
        breakpoint: '991px',
        numVisible: 3,
        numScroll: 1
      },
      {
        breakpoint: '767px',
        numVisible: 1,
        numScroll: 1
      }
    ];
  }
}


const mockTeam: Team = {
  team_ticker: "BOS",
  team_info: {
    id: 1610612738,
    full_name: "Boston Celtics",
    abbreviation: "BOS",
    nickname: "Celtics",
    city: "Boston",
    state: "MA",
    year_founded: 1946,
    arena: "TD Garden"
  },
  team_players: [
    {
      player_id: 1630552,
      player: "Marcus Smart",
      num: "26",
      position: "G",
      height: "6-3",
      weight: 220,
      age: 29,
      exp: "6"
    },
    {
      player_id: 123456,
      player: "Leo Baraldi",
      num: "37",
      position: "L",
      height: "6-11",
      weight: 210,
      age: 23,
      exp: "9"
    },
    {
      player_id: 1630552,
      player: "Marcus Smart",
      num: "26",
      position: "G",
      height: "6-3",
      weight: 220,
      age: 29,
      exp: "6"
    },
    {
      player_id: 123456,
      player: "Leo Baraldi",
      num: "37",
      position: "L",
      height: "6-11",
      weight: 210,
      age: 23,
      exp: "9"
    },
    {
      player_id: 1630552,
      player: "Marcus Smart",
      num: "26",
      position: "G",
      height: "6-3",
      weight: 220,
      age: 29,
      exp: "6"
    },
    {
      player_id: 123456,
      player: "Leo Baraldi",
      num: "37",
      position: "L",
      height: "6-11",
      weight: 210,
      age: 23,
      exp: "9"
    },

  ]
}

const mockMatches: Match[] = [
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
  },
  {
    "game_id": 12345,
    "match_up": "BKN - WAS",
    "date": "JUL 13, 2024",
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
  },
  {
    "game_id": 12345,
    "match_up": "BKN - WAS",
    "date": "JUL 14, 2024",
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
];
