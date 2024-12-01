class UniversityFactory:  # Создан базовый класс Университета
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

    def activate(self) -> None:
        print(f"{self.name} Двигается.")

    def info(self) -> str:
        return f"Название: {self.name}, Факультет: {self.capacity} "

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }

class University:
    def __init__(self, type, name, year):
        self.type = type
        self.name = name
        self.year = year

    def info(self):
        return f"Тип: {self.type}, Название: {self.name}, Год создания: {self.year}"
