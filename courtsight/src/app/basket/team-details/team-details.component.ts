import {Component, inject} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Title} from "@angular/platform-browser";
import {Team} from "../team";
import {TeamsService} from "../teams.service";

@Component({
  selector: 'app-team-details',
  standalone: true,
  imports: [],
  templateUrl: './team-details.component.html',
  styleUrl: './team-details.component.css'
})
export class TeamDetailsComponent {
  route: ActivatedRoute = inject(ActivatedRoute);
  teamsService = inject(TeamsService);
  team: Team | undefined;

  constructor(private titleService: Title) {
    this.titleService.setTitle('Team Details');
    const ticker = this.route.snapshot.params["ticker"];
    this.team = mockTeam; // TODO debug
    // this.teamsService.getTeamFromTicker(ticker, "2023-24").then((team: Team) => {
    //   this.team = team;
    // });
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
  ]
}
