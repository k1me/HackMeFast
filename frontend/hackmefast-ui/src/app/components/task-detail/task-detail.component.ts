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
  userInput: any;
  response: any;
  constructor(
    private route: ActivatedRoute,
    private taskService: TaskService,
    private router: Router,
    private http: HttpClient,
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
  
    const url = `http://localhost:8000/sqli/${this.task.difficulty}/search?username=${this.userInput}`;
  
    this.http.get(url).subscribe(
      (res) => {
        this.response = res;
      },
      (err) => {
        console.error('Hiba:', err);
      }
    );
  }
}
