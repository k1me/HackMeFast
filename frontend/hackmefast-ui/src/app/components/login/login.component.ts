import { HttpClient, HttpParams } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  username = '';
  password = '';
  errMsg = '';

  constructor(private http: HttpClient) {}

  onSubmit() {
    const formData = new FormData();
    formData.append('username',this.username);
    formData.append('password', this.password);
    this.http
      .post('http://localhost:8000/login/', formData,
        { withCredentials: true }
      )
      .subscribe({
        next: (res) => {
          console.log('Sikeres bejelentkezés:', res);
          this.errMsg = '';
        },
        error: (err) => {
          console.error('Hiba:', err);
          this.errMsg = 'Hibás felhasználónév vagy jelszó';
        },
      });
  }
}
