import {Component, Input} from '@angular/core';
import {DataViewModule} from "primeng/dataview";
import {Button} from "primeng/button";
import {DividerModule} from "primeng/divider";
import {RouterLink} from "@angular/router";
import {Match} from "../match";
import {CommonModule} from "@angular/common";
import {MatchComponent} from "./match/match.component";

@Component({
  selector: 'app-match-list',
  standalone: true,
  imports: [
    DataViewModule,
    Button,
    DividerModule,
    RouterLink,
    CommonModule,
    MatchComponent
  ],
  templateUrl: './match-list.component.html',
  styleUrl: './match-list.component.css'
})
export class MatchListComponent {
  @Input() matches!: Match[];
}
