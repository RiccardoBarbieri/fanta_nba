import {Component, Input, OnInit} from '@angular/core';
import {MeterGroupModule, MeterItem} from "primeng/metergroup";
import {CardModule} from "primeng/card";
import {DividerModule} from "primeng/divider";
import {colors} from "../../match-details.component";
import {DecimalPipe} from "@angular/common";

@Component({
  selector: 'app-stats-row',
  standalone: true,
  imports: [
    MeterGroupModule,
    CardModule,
    DividerModule,
    DecimalPipe
  ],
  templateUrl: './stats-row.component.html',
  styleUrl: './stats-row.component.css'
})
export class StatsRowComponent implements OnInit {
  @Input() row!: Row;

  meterValue: MeterItem[] = [];

  ngOnInit(): void {
    const total = this.row.leftValue + this.row.rightValue;
    const leftPerc = this.row.leftValue / total * 100;
    const rightPerc = 100 - leftPerc;

    if (this.row.leftValue > this.row.rightValue) {
      this.meterValue = [
        {color: colors.winningLeft, value: leftPerc},
        {color: colors.losingRight, value: rightPerc},
      ]
    } else if (this.row.leftValue < this.row.rightValue) {
      this.meterValue = [
        {color: colors.losingLeft, value: leftPerc},
        {color: colors.winningRight, value: rightPerc},
      ]
    } else {
      this.meterValue = [
        {color: colors.winningLeft, value: leftPerc},
        {color: colors.winningRight, value: rightPerc},
      ]
    }
  }
}


export interface Row {
  name: string,
  leftValue: number,
  rightValue: number,
}
