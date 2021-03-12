import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { PredictionService } from './prediction.service';

@Component({
  selector: 'app-prediction',
  templateUrl: './prediction.component.html',
  styleUrls: ['./prediction.component.css']
})
export class PredictionComponent implements OnInit {

  predictionForm: FormGroup;

  submitted = false;

  constructor(private service: PredictionService,
              private formBuilder: FormBuilder) {
    this.predictionForm = this.formBuilder.group({
      message: new FormControl("", [
        Validators.required
      ])
    })
  }

  messageValidation() {
    return (this.predictionForm.get("message").errors && this.submitted) ||
      (this.predictionForm.get("message").errors &&
        this.predictionForm.get("message").touched);
  }

  messageValid() {
    return !this.predictionForm.get("message").errors &&
      this.predictionForm.get("message").touched;
  }

  onSubmit() {
    this.submitted = true;

    if (this.predictionForm.valid) {
      this.service.getPrediction(this.predictionForm.value)
        .subscribe(response => {
          alert(response["prediction"])
        }, error => {
          alert(error);
        });
    }
  }

  ngOnInit(): void {
  }
}
