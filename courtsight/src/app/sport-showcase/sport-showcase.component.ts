import { Component } from '@angular/core';
import { SportDetailsComponent } from "../sport-details/sport-details.component";
import { Sport } from '../sport';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sport-showcase',
  standalone: true,
  imports: [CommonModule, SportDetailsComponent],
  templateUrl: './sport-showcase.component.html',
  styleUrl: './sport-showcase.component.css'
})
export class SportShowcaseComponent {
  availableSports: Sport[] = []

  constructor() {
    this.availableSports = [
      {
        name: "Basket",
        features: [
          {
            name: "Match predictions",
            available: true,
          },
          {
            name: "Bookmakers Integration",
            available: true,
          },
        ],
        url: '/basket'
      },
      {
        name: "Soccer",
        features: [
          {
            name: "Match predictions",
            available: false,
          },
          {
            name: "Bookmakers Integration",
            available: false,
          },
        ],
        url: undefined
      },
      {
        name: "Volleyball",
        features: [
          {
            name: "Match predictions",
            available: false,
          },
          {
            name: "Bookmakers Integration",
            available: true,
          },
        ],
        url: undefined,
      },
      {
        name: "Rugby",
        features: [
          {
            name: "Match predictions",
            available: false,
          },
          {
            name: "Bookmakers Integration",
            available: false,
          },
        ],
        url: undefined,
      },
    ]
  }
}
