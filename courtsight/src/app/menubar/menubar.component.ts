import {Component, inject, Input, OnInit} from '@angular/core';
import {SportsService} from '../shared/sports.service';
import {AvatarModule} from 'primeng/avatar';
import {InputTextModule} from 'primeng/inputtext';
import {MenubarModule} from 'primeng/menubar';
import {MenuItem} from 'primeng/api';
import {DropdownModule} from "primeng/dropdown";
import {FormsModule} from "@angular/forms";
import {Theme, ThemeService} from "../shared/theme.service";
import {CommonModule} from "@angular/common";


@Component({
  selector: 'app-menubar',
  standalone: true,
  imports: [
    MenubarModule,
    AvatarModule,
    InputTextModule,
    DropdownModule,
    FormsModule,
    CommonModule
  ],
  templateUrl: './menubar.component.html',
  styleUrl: './menubar.component.css'
})
export class MenubarComponent implements OnInit {
  @Input() title!: string;

  sportService: SportsService = inject(SportsService);

  items: MenuItem[] | undefined;

  themeService: ThemeService = inject(ThemeService);
  themes: Theme[] | undefined;
  selectedTheme: Theme | undefined;

  constructor() {

    this.themes = this.themeService.getAvailableThemes()
    this.selectedTheme = this.themes[0];
  }

  ngOnInit() {
    this.sportService.getAvailableSports().then(sports => {

      let sportItems: MenuItem[] = [];

      for (const sport of sports) {
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
    });
  }

  changeTheme() {
    if (this.selectedTheme) {
      this.themeService.switchTheme(this.selectedTheme.bundle);
    }
  }

}
