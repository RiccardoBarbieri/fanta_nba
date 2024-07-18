import {Component, Input} from '@angular/core';
import {CommonModule} from "@angular/common";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-details-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink
  ],
  templateUrl: './details-header.component.html',
  styleUrl: './details-header.component.css'
})
export class DetailsHeaderComponent {
  @Input() title: string | undefined= "";
  @Input() subtitle: string | undefined = "";
  @Input() items: Item[] = [];
  @Input() subtitleLink: string | undefined;
}

export interface Item {
  icon: string | null,
  value: string,
}
