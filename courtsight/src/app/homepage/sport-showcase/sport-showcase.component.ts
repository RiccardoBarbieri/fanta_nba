import { Component, inject } from '@angular/core';
import { SportDetailsComponent } from "../sport-details/sport-details.component";
import { AvailableSport } from '../../shared/sport';
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
  sportsList: AvailableSport[] = []

  constructor() {
    this.sportService.getAvailableSports().then(sports=>{
      this.sportsList = sports;
    });
  }
}
