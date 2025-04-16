import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { provideHttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { XssComponent } from './components/xss/xss.component';
import { SqliComponent } from './components/sqli/sqli.component';
import { CsrfComponent } from './components/csrf/csrf.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { DashboardInfoComponent } from './components/dashboard-info/dashboard-info.component';
import { TaskDetailComponent } from './components/task-detail/task-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    XssComponent,
    SqliComponent,
    CsrfComponent,
    TaskListComponent,
    DashboardInfoComponent,
    TaskDetailComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserModule,
    FormsModule,
  ],
  providers: [provideHttpClient()],
  bootstrap: [AppComponent]
})
export class AppModule { }
