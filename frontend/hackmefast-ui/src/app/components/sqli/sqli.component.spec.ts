import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SqliComponent } from './sqli.component';

describe('SqliComponent', () => {
  let component: SqliComponent;
  let fixture: ComponentFixture<SqliComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SqliComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SqliComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
