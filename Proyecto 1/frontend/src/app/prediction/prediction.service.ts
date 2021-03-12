import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment as env } from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  constructor(private http: HttpClient) { }

  getPrediction(message) {
    let body = {
      "message": message
    }

    return this.http.post(env.apiUrl + "/api/prediction", body);
  }
}
