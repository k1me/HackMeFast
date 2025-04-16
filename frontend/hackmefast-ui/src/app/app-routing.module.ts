import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { DashboardInfoComponent } from './components/dashboard-info/dashboard-info.component';
import { TaskDetailComponent } from './components/task-detail/task-detail.component';
import { SqliComponent } from './components/sqli/sqli.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  {
    path: 'dashboard',
    component: DashboardComponent,
    children: [
      {
        path: '',
        component: DashboardInfoComponent,
      },
      { path: 'xss', component: TaskListComponent, data: { category: 'XSS' } },
      {
        path: 'sqli',
        component: SqliComponent,
        data: { category: 'SQLi' },
        children: [
          { path: '', component: TaskListComponent },
          { path: 'task/:id', component: TaskDetailComponent },
        ],
      },
      {
        path: 'csrf',
        component: TaskListComponent,
        data: { category: 'CSRF' },
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
