import { Injectable } from '@angular/core';
import { Sport } from './sport';

@Injectable({
  providedIn: 'root'
})
export class SportsService {

  sports: Sport[] = []

  constructor() {
    this.sports = [
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

  getAllSports() {
    return this.sports;
  }
}
