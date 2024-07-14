import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatsRowComponent } from './stats-row.component';

describe('StatsRowComponent', () => {
  let component: StatsRowComponent;
  let fixture: ComponentFixture<StatsRowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StatsRowComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StatsRowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
