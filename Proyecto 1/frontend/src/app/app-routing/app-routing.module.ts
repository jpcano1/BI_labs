import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { PredictionComponent } from '../prediction/prediction.component';
import { LabelerComponent } from '../labeler/labeler.component';

const routes = [
  {
    path: "prediction",
    component: PredictionComponent,
    data: {
      animation: "PredictionPage"
    }
  },
  {
    path: "labeler",
    component: LabelerComponent,
    data: {
      animation: "LabelerPage"
    }
  },
  {
    path: "",
    redirectTo: "prediction",
    pathMatch: "full"
  }
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(
      routes, {
        onSameUrlNavigation: "reload"
      })
  ]
})
export class AppRoutingModule { }
