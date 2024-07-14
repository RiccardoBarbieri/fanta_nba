import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-stats-row',
  standalone: true,
  imports: [],
  templateUrl: './stats-row.component.html',
  styleUrl: './stats-row.component.css'
})
export class StatsRowComponent implements OnInit {
  @Input() row!: Row;
  @Input() alignment: "left" | "right" = "left";
  flex_class: string | undefined;

  ngOnInit(): void {
    switch (this.alignment) {
      case "left":
        this.flex_class = "flex-row"; break;
      case "right":
        this.flex_class = "flex-row-reverse"; break;
    }
  }
}

export interface Row {
  name: string,
  value: string | number,
}
