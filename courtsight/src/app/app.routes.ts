import {Routes} from '@angular/router';
import {HomeComponent} from "./homepage/home/home.component";
import {HomeComponent as BasketHome} from "./basket/home/home.component";
import {TeamDetailsComponent} from "./basket/team-details/team-details.component";
import {MatchDetailsComponent} from "./basket/match-details/match-details.component";
import {PlayerDetailsComponent} from "./basket/player-details/player-details.component";
import {SimpleRouterComponent} from "./shared/simple-router/simple-router.component";

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
        component: SimpleRouterComponent,
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
            title: "Match",
            data: {breadcrumb: 'Match'}
          },
          {
            path: 'team/:ticker',
            component: SimpleRouterComponent,
            title: "Team",
            data: {breadcrumb: 'Team'},
            children: [
              {
                path: '',
                component: TeamDetailsComponent,
                data: {breadcrumb: ''}
              },
              {
                path: 'player/:id',
                component: PlayerDetailsComponent,
                data: {breadcrumb: 'Player'}
              },
            ]
          },
        ]
      },
    ]
  },
];
