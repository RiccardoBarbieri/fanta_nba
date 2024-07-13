import {Routes} from '@angular/router';
import {HomeComponent} from "./homepage/home/home.component";
import {HomeComponent as BasketHome} from "./basket/home/home.component";
import {TeamDetailsComponent} from "./basket/team-details/team-details.component";

export const routes: Routes = [
  {
    path: "",
    component: HomeComponent,
    title: "Home Page"
  },
  {
    path: "basket",
    component: BasketHome,
    title: "Basketball",
  },
  {
    path: 'basket/match/:id',
    component: HomeComponent,
  },
  {
    path: 'basket/team/:ticker',
    component: TeamDetailsComponent,
  },
];
