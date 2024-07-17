import {Routes} from '@angular/router';
import {HomeComponent} from "./homepage/home/home.component";
import {HomeComponent as BasketHome} from "./basket/home/home.component";
import {TeamDetailsComponent} from "./basket/team-details/team-details.component";
import {MatchDetailsComponent} from "./basket/match-details/match-details.component";
import {BasketComponent} from "./basket/basket.component";

export const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        component: HomeComponent,
        title: "Home Page",
        data: {breadcrumb: 'Home'}
      },
      {
        path: "basketball",
        component: BasketComponent,
        title: "Basketball",
        data: {breadcrumb: 'Basketball'},
        children: [
          {
            path: '',
            component: BasketHome,
            data: {breadcrumb: ''}
          },
          {
            path: 'match/:id/:date',
            component: MatchDetailsComponent,
            data: {breadcrumb: 'Match'}
          },
          {
            path: 'team/:ticker',
            component: TeamDetailsComponent,
            data: {breadcrumb: 'Team'}
          },
        ]
      },
    ]
  },
];
