import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

let apiUrl = "http://localhost:5000"

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  constructor(private http: HttpClient) { }

  getPrediction(message) {
    let body = {
      "message": message
    }

    return this.http.post(apiUrl + "/api/prediction", body);
  }
}
