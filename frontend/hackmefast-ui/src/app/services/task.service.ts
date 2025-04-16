import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  private apiUrl = 'http://localhost:8000/tasks';

  constructor(private http: HttpClient) {}

  getTasks(category: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}?category=${category}`);
  }

  getTaskById(id: number) {
    return this.http.get<any>(`${this.apiUrl}/${id}`)
  }
}
