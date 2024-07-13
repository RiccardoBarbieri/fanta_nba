import {Component, OnInit} from '@angular/core';
import {StandingsComponent} from "../standings/standings.component";
import {CardModule} from "primeng/card";
import {CommonModule, DatePipe} from "@angular/common";
import {DividerModule} from "primeng/divider";
import {Match} from "../match";
import {DataViewModule} from "primeng/dataview";
import {TagModule} from "primeng/tag";
import {RouterLink} from "@angular/router";
import {Button} from "primeng/button";


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
    Button
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  today = new Date();
  matches!: Match[];

  navigateToMatch(match_id: number) {

  }

  ngOnInit() {
    this.matches = [
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
    ]
  }
}
