import { Injectable } from '@angular/core';
import {Vector} from "./vector";

@Injectable({
  providedIn: 'root'
})
export class PredictionsService {
    url: string = "https://nba-api.orangewave-05a306f8.westeurope.azurecontainerapps.io/score";

  async getPredictionForMatch(vector: Vector): Promise<number> {

    const data = await fetch(this.url, {
      method: "POST",
      body: JSON.stringify(vector),
      headers: {"Content-Type": "application/json"}
    })
    return await data.json();
  }
}
