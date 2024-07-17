import {Component, Input} from '@angular/core';
import {Match} from "../../match";
import {DividerModule} from "primeng/divider";
import {Button} from "primeng/button";
import {RouterLink} from "@angular/router";
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-match',
  standalone: true,
  imports: [
    DividerModule,
    Button,
    RouterLink,
    CommonModule
  ],
  templateUrl: './match.component.html',
  styleUrl: './match.component.css'
})
export class MatchComponent {
  @Input() match!:Match;
}
