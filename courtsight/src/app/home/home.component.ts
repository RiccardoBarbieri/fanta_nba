import { Component } from '@angular/core';
import { SportShowcaseComponent } from "../sport-showcase/sport-showcase.component";


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [SportShowcaseComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
