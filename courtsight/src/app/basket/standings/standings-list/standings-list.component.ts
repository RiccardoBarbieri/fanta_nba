import {Component, Input} from '@angular/core';
import {CardModule} from "primeng/card";
import {TableModule} from "primeng/table";
import {Button} from "primeng/button";
import {RouterLink} from "@angular/router";
import {NgClass} from "@angular/common";
import {PanelModule} from "primeng/panel";
import {FieldsetModule} from "primeng/fieldset";
import {TeamStandings} from "../../standings";

@Component({
  selector: 'app-standings-list',
  standalone: true,
  imports: [
    CardModule,
    TableModule,
    Button,
    RouterLink,
    NgClass,
    PanelModule,
    FieldsetModule
  ],
  templateUrl: './standings-list.component.html',
  styleUrl: './standings-list.component.css'
})
export class StandingsListComponent {
  @Input() title! : string;
  @Input() teams! : TeamStandings[];
}
