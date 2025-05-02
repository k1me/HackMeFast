class Task:
    def __init__(self, id, title, difficulty, description, category, type):
        self.id = id # endpoint meghatarozasra, illetve, hogy hanyadik feladat
        self.title = title
        self.difficulty = difficulty
        self.description = description
        self.category = category # maga a kategoria, hogy meg lehessen kulonboztetni a feladatokat kategoria alapjan
        self.type = type # tipus pl.: bejelentkezos (1 parameteres, 2 parameteres, ...)  