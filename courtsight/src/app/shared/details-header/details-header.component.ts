import {Component, Input} from '@angular/core';
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-details-header',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './details-header.component.html',
  styleUrl: './details-header.component.css'
})
export class DetailsHeaderComponent {
  @Input() title: string | undefined= "";
  @Input() subtitle: string | undefined = "";
  @Input() items: Item[] = [];

}

export interface Item {
  icon: string | null,
  value: string,
}
