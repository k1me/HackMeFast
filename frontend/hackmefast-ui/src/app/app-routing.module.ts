import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { XssComponent } from './pages/xss/xss.component';
import { CsrfComponent } from './pages/csrf/csrf.component';
import { SqliComponent } from './pages/sqli/sqli.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent},
  { path: 'dashboard', component: DashboardComponent,
    children: [
      {path: 'xss', component: XssComponent},
      {path: 'sqli', component: SqliComponent},
      {path: 'csrf', component: CsrfComponent}
    ]
   }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
