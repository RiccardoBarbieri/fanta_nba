import {Component, inject} from '@angular/core';
import {DetailsHeaderComponent, Item} from "../../shared/details-header/details-header.component";
import {PlayerStats} from "../stats";
import {PlayersService} from "../players.service";
import {ActivatedRoute} from "@angular/router";
import {TimeTravelService} from "../../shared/time-travel.service";
import {Player} from "../player";
import {Team} from "../team";
import {TeamsService} from "../teams.service";
import {PlayerStatsComponent} from "./player-stats/player-stats.component";
import {CommonModule} from "@angular/common";
import {CardModule} from "primeng/card";
import {DividerModule} from "primeng/divider";
import {TimeTravelComponent} from "../../shared/time-travel/time-travel.component";

@Component({
  selector: 'app-player-details',
  standalone: true,
  imports: [
    DetailsHeaderComponent,
    PlayerStatsComponent,
    CommonModule,
    CardModule,
    DividerModule,
    TimeTravelComponent
  ],
  templateUrl: './player-details.component.html',
  styleUrl: './player-details.component.css'
})
export class PlayerDetailsComponent {
  route: ActivatedRoute = inject(ActivatedRoute);

  teamsService = inject(TeamsService);
  playerService = inject(PlayersService);
  timetravelService = inject(TimeTravelService);

  team: Team | undefined;
  player: Player | undefined;
  playerStats: PlayerStats | undefined;
  header_items: Item[] = [];

  average_stats: any[] = []

  constructor() {
   this.refreshStats()
  }

  refreshStats() {
    const player_id = this.route.snapshot.params["id"];

    this.route.parent!.params.subscribe(params => {
      const ticker = params['ticker'];

      this.teamsService.getTeamFromTicker(ticker, "2023-24").then((team: Team) => {
        this.team = team;
        this.player = team.team_players.find((p) => String(p.player_id) === player_id);

        if (this.player) {
          this.header_items = [
            {
              icon: 'pi pi-info-circle', value: `${this.player.age} y/0`,
            },
            {
              icon: null, value: `${this.player.weight} lb`,
            },
            {
              icon: null, value: `${this.player.height} ft`,
            },
          ]
        }

        this.playerService.getPlayerStatsById(player_id, "2023-24", this.timetravelService.getDateString(), "5").then(playerStats => {
          this.playerStats = playerStats;
          this.average_stats = [
            {
              value: `${this.player?.exp} years`,
              name: "Experience",
            },
            {
              value: playerStats.average.pts,
              name: "PPG",
            },
            {
              value: playerStats.average.reb,
              name: "RPG",
            },
            {
              value: playerStats.average.ast,
              name: "APG",
            },
            {
              value: playerStats.average.blk,
              name: "BLK",
            },
          ]
        })
      })
    })
  }

}
