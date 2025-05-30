import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TaskService } from '../../services/task.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-task-detail',
  standalone: false,
  templateUrl: './task-detail.component.html',
  styleUrl: './task-detail.component.css',
})
export class TaskDetailComponent implements OnInit {
  task: any;
  username: any;
  password: any;
  response: any;
  constructor(
    private route: ActivatedRoute,
    private taskService: TaskService,
    private router: Router,
    private http: HttpClient
  ) {}
  ngOnInit() {
    const id = +this.route.snapshot.paramMap.get('id')!;
    this.taskService.getTaskById(id).subscribe((task) => (this.task = task));
  }

  goBack() {
    this.router.navigate(['../../'], { relativeTo: this.route });
  }

  submitSQLiTask() {
    if (!this.task?.id) {
      console.error('Nincs task id(?)');
      return;
    }
    // ide egy post check még kell
    const url = `http://localhost:8000/sqli/${this.task.id}?username=${this.username}&password=${this.password}`;

    this.http.get(url).subscribe(
      (res) => {
        this.response = res;
      },
      (err) => {
        this.response = err;
        console.error('Hiba:', err);
      }
    );
  }
}
