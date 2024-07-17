import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TimeTravelService {
  date: Date = new Date("2023-11-05");

  constructor() { }

  setDate(date: Date) {
    this.date = date;
  }


}
