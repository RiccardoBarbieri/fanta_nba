import {Component, inject} from '@angular/core';
import {ActivatedRoute, RouterLink} from "@angular/router";
import {MatchesService} from "../matches.service";
import {Match} from "../match";
import {DividerModule} from "primeng/divider";
import {ActualAndLastMatchStats, MatchStats} from "../stats";
import {FieldsetModule} from "primeng/fieldset";
import {CommonModule, DatePipe} from "@angular/common";
import {SplitterModule} from "primeng/splitter";
import {StatsTableComponent} from "./stats-table/stats-table.component";
import {MeterGroupModule, MeterItem} from "primeng/metergroup";
import {PanelModule} from "primeng/panel";
import {CardModule} from "primeng/card";
import {OddsService} from "../odds.service";
import {Vector} from "../vector";
import {PredictionsService} from "../predictions.service";
import {Button} from "primeng/button";
import {SkeletonModule} from "primeng/skeleton";
import {Odds} from "../odds";
import {TableModule} from "primeng/table";
import {BookmakersListComponent} from "../../shared/bookmakers-list/bookmakers-list.component";

@Component({
  selector: 'app-match-details',
  standalone: true,
  imports: [
    DividerModule,
    RouterLink,
    FieldsetModule,
    DatePipe,
    SplitterModule,
    StatsTableComponent,
    MeterGroupModule,
    CommonModule,
    PanelModule,
    CardModule,
    Button,
    SkeletonModule,
    TableModule,
    BookmakersListComponent
  ],
  templateUrl: './match-details.component.html',
  styleUrl: './match-details.component.css'
})
export class MatchDetailsComponent {
  route: ActivatedRoute = inject(ActivatedRoute);

  matchesService = inject(MatchesService);
  oddsService = inject(OddsService);
  predictionsService = inject(PredictionsService);

  match: Match | undefined;
  matchStats: MatchStats | undefined;
  meterValue: MeterItem[] = [];
  odds: Odds | undefined;

  computed: boolean = false
  loading: boolean = false;
  prediction_message = "";
  prediction_result = "";


  constructor() {
    const match_id = this.route.snapshot.params["id"];
    const match_date = this.route.snapshot.params["date"];

    this.matchesService.getMatchStatsById(match_id, match_date).then((matches: ActualAndLastMatchStats) => {
      this.matchStats = matches.actual_match_stats

      let homePts = this.matchStats.by_home_stats.pts;
      let awayPts = this.matchStats.by_away_stats.pts;
      let total = homePts + awayPts;

      this.meterValue = [
        {label: '', value: homePts / total * 100, color: homePts >= awayPts ? colors.winningLeft : colors.losingLeft},
        {label: '', value: awayPts / total * 100, color: homePts >= awayPts ? colors.losingRight : colors.winningRight},
      ]

      this.matchesService.getMatchesByDate(this.matchStats.global_stats.game_date, this.matchStats.global_stats.game_date).then(matches => {
        this.match = matches.find(m => m.game_id === match_id);
      })

      const event_id: string = `${this.matchStats?.by_home_stats.team_abbreviation}FAKE${this.matchStats?.by_away_stats.team_abbreviation}`;
      this.oddsService.getOddsForMatch(event_id).then((odds: Odds[]) => {
        this.odds = odds[0];
      })
    });
  }

  getPrediction() {
    this.loading = true;

    if (this.matchStats) {
      this.matchesService.getFeatureVectorForMatch(this.matchStats.by_home_stats.team_abbreviation, this.matchStats.by_away_stats.team_abbreviation, "2023-24", this.matchStats.global_stats.game_date)
        .then((vector: Vector) => {
          if (vector.game_id === null) {
            this.prediction_message = "There was an error retrieving the feature vector"
            this.loading = false;
            this.computed = true;
          } else {
            this.predictionsService.getPredictionForMatch(vector).then((prediction) => {
              this.loading = false;
              this.computed = true;
              if (prediction > 0) {
                this.prediction_message = `${this.matchStats?.by_home_stats.team_name} are forecast to win!`
                this.prediction_result = String(Math.abs(prediction));
              } else if (prediction < 0) {
                this.prediction_message = `${this.matchStats?.by_away_stats.team_name} are forecast to win!`
                this.prediction_result = String(Math.abs(prediction));
              } else {
                this.prediction_message = "The result of the match could not be predicted"
              }
            })
          }
        });
    }
  }
}

export const colors = {
  winningLeft: "#3bc21d",
  losingLeft: "rgba(73,225,11,0.25)",
  winningRight: "#eb9c08",
  losingRight: "rgba(235,156,8,0.25)",
}
