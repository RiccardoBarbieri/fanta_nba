import {Component, Input, OnInit} from '@angular/core';
import {TableModule} from "primeng/table";
import {DecimalPipe} from "@angular/common";
import {Odds} from "../../basket/odds";

@Component({
  selector: 'app-bookmakers-list',
  standalone: true,
  imports: [
    TableModule,
    DecimalPipe
  ],
  templateUrl: './bookmakers-list.component.html',
  styleUrl: './bookmakers-list.component.css'
})
export class BookmakersListComponent implements OnInit {
  @Input() odds!: Odds;
  @Input() home_team!: string;
  @Input() away_team!: string;

  bookmakers_list: any[] = [];

  ngOnInit() {
    let max = 0;
    let min = 100000
    for (let bookmaker of this.odds.bookmakers) {
      const home_quota = bookmaker.markets[0].outcomes.find((o) => o.name === this.home_team)?.price!;
      const away_quota = bookmaker.markets[0].outcomes.find((o) => o.name === this.away_team)?.price!;
      if (home_quota < min) {
        min = home_quota;
      }
      if (away_quota < min) {
        min = away_quota;
      }
      if (home_quota > max) {
        max = home_quota;
      }
      if (away_quota > max) {
        max = away_quota;
      }
      this.bookmakers_list.push({
        name: bookmaker.title,
        url: bookmaker.url,
        home_team_quota: {
          value: home_quota, color: "text-900"
        },
        away_team_quota: {
          value: away_quota, color: "text-900"
        },
      })
    }

    for (let item of this.bookmakers_list) {
      if (item.home_team_quota.value === max) {
        item.home_team_quota.color = "text-green-600"
      }
      if (item.home_team_quota.value === min) {
        item.home_team_quota.color = "text-red-500"
      }
      if (item.away_team_quota.value === max) {
        item.away_team_quota.color = "text-green-600"
      }
      if (item.away_team_quota.value === min) {
        item.away_team_quota.color = "text-red-500"
      }
    }
  }
}
