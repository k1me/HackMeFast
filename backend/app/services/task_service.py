from app.models.task import Task

tasks = [
    Task(
        1,
        "Klasszikus Login",
        0,
        "Egy egyszerű bejelentkezési oldalt kaptál. Sajnos az SQL lekérdezés nem túl biztonságos... \
            Be tudsz úgy lépni, hogy nem ismered az admin felhasználó jelszavát? Ha sikerül, kapsz egy flag-et.",
        "SQLi",
        2,
    ),
    Task(
        2,
        "Keresés Felhasználók Közt",
        0,
        "Egy keresőmező segítségével kereshetsz felhasználónév alapján. Vajon van lehetőség arra, \
            hogy más felhasználók adataihoz hozzáférj anélkül, hogy tudnád a pontos nevüket? \
            Az egyik felhasználó adatai között találsz egy flag-et.",
        "SQLi",
        1,
    ),
    Task(
        3,
        "Adatszivárgás UNION-nal",
        1,
        "Egy felhasználói ID (int) alapján lekérdezhetsz adatokat az adatbázisból. A lekérdezés viszont nem védi magát \
            a UNION SELECT támadások ellen... \
            Tudsz olyan adatot kinyerni, ami nem is része az eredeti lekérdezésnek?",
        "SQLi",
        1,
    ),
    Task(
        4,
        "Blind SQLi - Boolean alapú",
        2,
        "A válasz minden esetben ugyanaz, de a háttérben különbség van: vajon meg tudod állapítani, hogy egy adott "
        "felhasználó létezik-e, pusztán a válaszüzenetek alapján?",
        "SQLi",
        1,
    ),
    Task(
        5,
        "WAF Bypass",
        3,
        "Az alkalmazás egy egyszerű tűzfalat (WAF-ot) használ, ami kiszűri a jól ismert SQL kulcsszavakat. "
        "Ennek ellenére létezik mód arra, hogy megkerüld a szűrőt, és bejuss a rendszerbe?",
        "SQLi",
        2,
    ),
    Task(
        6,
        "Jelszómódosítás",
        2,
        "Egy naplózó funkció egyetlen bemenetet vesz át – de ezt nem megfelelően szűri. Meg tudod változtatni "
        "a sysadmin felhasználó jelszavát anélkül, hogy hitelesítve lennél?",
        "SQLi",
        1,
    ),
]


def get_tasks_by_category(category: str):
    if category:
        return [task for task in tasks if task.category == category]
    return tasks


def get_task_by_id(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)
