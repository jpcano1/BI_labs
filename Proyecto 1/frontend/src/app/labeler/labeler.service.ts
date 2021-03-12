import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

let apiUrl = "http://localhost:5000"

@Injectable({
  providedIn: 'root'
})
export class LabelerService {

  constructor(private http: HttpClient) { }

  labelMessage(message, label) {
    let body = {
      "message": message,
      "label": label
    }
    return this.http.post(apiUrl + "/api/labeler", body);
  }
}
