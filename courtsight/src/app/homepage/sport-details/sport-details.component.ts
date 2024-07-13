import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { Sport } from '../../shared/sport';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-sport-detail',
  standalone: true,
  imports: [CommonModule, ButtonModule, RouterModule],
  templateUrl: './sport-details.component.html',
  styleUrl: './sport-details.component.css'
})
export class SportDetailsComponent {
  @Input() sport!: Sport;

  getIcon(value: boolean):string {
    if (value) {
      return "pi pi-check-circle text-green-500 mr-2"
    } else {
      return "pi pi-ban text-red-500 mr-2";
    }
  }
}
