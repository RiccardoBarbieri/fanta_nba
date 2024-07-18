import {Component, Input} from '@angular/core';
import {TableModule} from "primeng/table";
import {PlayerMatchStats} from "../../stats";
import {RouterLink} from "@angular/router";
import {DatePipe} from "@angular/common";

@Component({
  selector: 'app-player-stats',
  standalone: true,
  imports: [
    TableModule,
    RouterLink,
    DatePipe
  ],
  templateUrl: './player-stats.component.html',
  styleUrl: './player-stats.component.css'
})
export class PlayerStatsComponent {
  @Input() title : string = "";
  @Input() rows! : PlayerMatchStats[];

  constructor() {
  }

}
