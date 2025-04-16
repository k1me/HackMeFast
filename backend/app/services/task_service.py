from app.models.task import Task

tasks = [
    Task(1, "SQL Injection", "easy", "SQLi easy feladat leírása", "SQLi"),
    Task(2, "SQL Injection", "medium", "SQLi medium feladat leírása", "SQLi"),
    Task(3, "SQL Injection", "hard", "SQLi medium feladat leírása", "SQLi"),
]


def get_tasks_by_category(category: str):
    if category:
        return [task for task in tasks if task.category == category]
    return tasks


def get_task_by_id(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)
