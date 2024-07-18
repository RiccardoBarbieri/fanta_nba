import { Component } from '@angular/core';
import {RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-simple-router',
  standalone: true,
  imports: [
    RouterOutlet
  ],
  templateUrl: './simple-router.component.html',
  styleUrl: './simple-router.component.css'
})
export class SimpleRouterComponent {

}
