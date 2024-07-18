import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerDetailsComponent } from './player-details.component';

describe('PlayerDetailsComponent', () => {
  let component: PlayerDetailsComponent;
  let fixture: ComponentFixture<PlayerDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PlayerDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlayerDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
