import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StandingsListComponent } from './standings-list.component';

describe('StandingsListComponent', () => {
  let component: StandingsListComponent;
  let fixture: ComponentFixture<StandingsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StandingsListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StandingsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
