import {Component, Input, OnInit} from '@angular/core';
import {CarouselModule} from "primeng/carousel";
import {Player} from "../../player";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-player-showcase',
  standalone: true,
  imports: [
    CarouselModule,
    RouterLink
  ],
  templateUrl: './player-showcase.component.html',
  styleUrl: './player-showcase.component.css'
})
export class PlayerShowcaseComponent implements OnInit {
  @Input() players!: Player[];

  responsiveOptions: any[] | undefined;

  ngOnInit(): void {
    this.responsiveOptions = [
      {
        breakpoint: '1600px',
        numVisible: 6,
        numScroll: 6
      },
      {
        breakpoint: '1400px',
        numVisible: 5,
        numScroll: 5
      },
      {
        breakpoint: '1200px',
        numVisible: 4,
        numScroll: 4
      },
      {
        breakpoint: '1000px',
        numVisible: 3,
        numScroll: 3
      },
      {
        breakpoint: '800px',
        numVisible: 2,
        numScroll: 2
      },
      {
        breakpoint: '600px',
        numVisible: 1,
        numScroll: 1
      }
    ];
  }
}
