import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import * as $ from "jquery";
import { LabelerService } from './labeler.service';

@Component({
  selector: 'app-labeler',
  templateUrl: './labeler.component.html',
  styleUrls: ['./labeler.component.css']
})
export class LabelerComponent implements OnInit {

  submitted = false;

  labelerForm: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private service: LabelerService) {
    this.labelerForm = this.formBuilder.group({
      "message": formBuilder.control("", [
        Validators.required
      ])
    })
  }

  messageValidation() {
    return (this.labelerForm.get("message").errors && this.submitted) ||
      (this.labelerForm.get("message").errors &&
        this.labelerForm.get("message").touched);
  }

  messageValid() {
    return !this.labelerForm.get("message").errors &&
      this.labelerForm.get("message").touched;
  }

  onSubmit() {
    this.submitted = true;

    if (this.labelerForm.valid) {
      let spam = $("#spam").is(":checked")? 1: 0;
      let message = this.labelerForm.get("message").value;

      this.service.labelMessage(message, spam)
        .subscribe(response => {
          alert(response["message"]);
        });
    }
  }

  ngOnInit(): void {
  }
}
