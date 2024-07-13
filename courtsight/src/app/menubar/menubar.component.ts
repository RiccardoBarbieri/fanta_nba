import { Component, inject, Input, input } from '@angular/core';
import { Sport } from '../shared/sport';
import { SportsService } from '../shared/sports.service';
import { AvatarModule } from 'primeng/avatar';
import { InputTextModule } from 'primeng/inputtext';
import { MenubarModule } from 'primeng/menubar';
import { MenuItem } from 'primeng/api';


@Component({
  selector: 'app-menubar',
  standalone: true,
  imports: [
    MenubarModule,
    AvatarModule,
    InputTextModule
  ],
  templateUrl: './menubar.component.html',
  styleUrl: './menubar.component.css'
})
export class MenubarComponent {
  @Input() title!: string;

  sportService: SportsService = inject(SportsService);
  sportsList: Sport[] = []

  items: MenuItem[] | undefined;

  constructor() {
    this.sportsList = this.sportService.getAllSports();
  }


  ngOnInit() {
    let sportItems: MenuItem[] = [];

    for (const sport of this.sportsList) {
      sportItems.push({
        label: sport.name,
        route: sport.url,
        disabled: sport.url === undefined
      });
    }

    this.items = [
      {
        label: 'Home',
        icon: 'pi pi-home',
        route: '/'
      },
      {
        label: 'Sports',
        icon: 'pi pi-trophy',
        items: sportItems,
      },
    ]
  }
}
