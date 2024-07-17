import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookmakersListComponent } from './bookmakers-list.component';

describe('BookmakersListComponent', () => {
  let component: BookmakersListComponent;
  let fixture: ComponentFixture<BookmakersListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BookmakersListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BookmakersListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
