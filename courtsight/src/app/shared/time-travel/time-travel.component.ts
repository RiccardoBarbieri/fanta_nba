import {Component, EventEmitter, inject, Output} from '@angular/core';
import {DividerModule} from "primeng/divider";
import {CalendarModule} from "primeng/calendar";
import {FormsModule} from "@angular/forms";
import {TimeTravelService} from "../time-travel.service";

@Component({
  selector: 'app-time-travel',
  standalone: true,
  imports: [
    DividerModule,
    CalendarModule,
    FormsModule
  ],
  templateUrl: './time-travel.component.html',
  styleUrl: './time-travel.component.css'
})
export class TimeTravelComponent {
  @Output() onDateUpdate: EventEmitter<any> = new EventEmitter();

  timetravelService = inject(TimeTravelService);
  date: Date;

  constructor() {
    this.date = this.timetravelService.date;
  }

  updateDate() {
    this.timetravelService.setDate(this.date);
    this.onDateUpdate.emit()
  }
}
