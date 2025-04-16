import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-service-list',
  standalone: false,
  templateUrl: './task-list.component.html',
  styleUrl: './task-list.component.css',
})
export class TaskListComponent implements OnInit {
  tasks: any[] = [];
  categories: string[] = ['SQLi', 'XSS', 'CSRF'];
  selectedCategory: string = 'SQLi';

  constructor(private taskService: TaskService, private router: Router, private route: ActivatedRoute) {}
  ngOnInit(): void {
    this.route.data.subscribe(data => {
      this.selectedCategory = data['category'];
      this.getTasksByCategory();
    });

  }

  getTasksByCategory(): void {
    this.taskService.getTasks(this.selectedCategory).subscribe(
      (tasks) => {
        this.tasks = tasks;
      },
      (error) => {
        console.error('Hiba történt a feladatok lekérdezésekor: ', error);
      }
    );
  }

  goToTaskPage(id: number): void {
    this.router.navigate([`/task/${id}`]);
  }
}
