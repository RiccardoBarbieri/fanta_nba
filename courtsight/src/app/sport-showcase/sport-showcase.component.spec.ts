import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SportShowcaseComponent } from './sport-showcase.component';

describe('SportShowcaseComponent', () => {
  let component: SportShowcaseComponent;
  let fixture: ComponentFixture<SportShowcaseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SportShowcaseComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SportShowcaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
