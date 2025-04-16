from app.models.task import Task

tasks = [
    Task(
        1,
        "SQL Injection",
        "easy",
        "Egy egyszerű felhasználónév‑jelszó alapú bejelentkezési űrlappal dolgozol, ahol nincsen semmilyen bemenetszűrés. A célod, hogy jelszó ismerete nélkül belépj egy tetszőleges felhasználó (például az admin) nevében.",
        "SQLi",
    ),
    Task(
        2,
        "SQL Injection",
        "medium",
        "Ebben a feladatban a bejelentkezési logika ugyanúgy felhasználónév‑jelszó párral dolgozik, de karaktertiltó-környezet lett bevezetve. A cél, hogy mégis sikerüljön SQL injection-nel megkerülni a bejelentkezést.",
        "SQLi",
    ),
    Task(
        3,
        "SQL Injection",
        "hard",
        "Egy bejelentkezési felület segítségével tudsz lekérdezni felhasználókat az adatbázisból. A szerver nem használ paraméterezett lekérdezést, hanem a username és password mezőket közvetlenül illeszti be az SQL utasításba.",
        "SQLi",
    ),
]


def get_tasks_by_category(category: str):
    if category:
        return [task for task in tasks if task.category == category]
    return tasks


def get_task_by_id(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)
