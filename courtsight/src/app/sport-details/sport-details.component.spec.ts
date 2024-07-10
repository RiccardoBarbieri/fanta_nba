import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SportDetailsComponent } from './sport-details.component';

describe('SportDetailComponent', () => {
  let component: SportDetailsComponent;
  let fixture: ComponentFixture<SportDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SportDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SportDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
