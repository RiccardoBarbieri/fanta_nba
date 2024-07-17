import { TestBed } from '@angular/core/testing';

import { TimeTravelService } from './time-travel.service';

describe('TimeTravelService', () => {
  let service: TimeTravelService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TimeTravelService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
