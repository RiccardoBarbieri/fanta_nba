import { Injectable } from '@angular/core';
import {getFormattedDate} from "./utils";

@Injectable({
  providedIn: 'root'
})
export class TimeTravelService {
  date: Date = new Date("2023-11-05");

  constructor() { }

  setDate(date: Date) {
    this.date = date;
  }

  getDateString() {
    return getFormattedDate(this.date)
  }


}
