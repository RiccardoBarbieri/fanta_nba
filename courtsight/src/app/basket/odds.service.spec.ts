import { TestBed } from '@angular/core/testing';

import { OddsService } from './odds.service';

describe('OddsService', () => {
  let service: OddsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OddsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
