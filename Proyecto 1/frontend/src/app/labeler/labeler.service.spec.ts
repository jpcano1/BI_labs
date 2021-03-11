import { TestBed } from '@angular/core/testing';

import { LabelerService } from './labeler.service';

describe('LabelerService', () => {
  let service: LabelerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LabelerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
