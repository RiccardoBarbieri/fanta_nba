import { Component, inject } from '@angular/core';
import { SportDetailsComponent } from "../sport-details/sport-details.component";
import { Sport } from '../../shared/sport';
import { CommonModule } from '@angular/common';
import { SportsService } from '../../shared/sports.service';

@Component({
  selector: 'app-sport-showcase',
  standalone: true,
  imports: [CommonModule, SportDetailsComponent],
  templateUrl: './sport-showcase.component.html',
  styleUrl: './sport-showcase.component.css'
})
export class SportShowcaseComponent {
  sportService: SportsService = inject(SportsService);
  sportsList: Sport[] = []

  constructor() {
    this.sportsList = this.sportService.getAllSports();
  }
}
