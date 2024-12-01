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

class IIT(UniversityFactory):  # Далее идут наследованные от UniversityFactory классы
    def activate(self) -> None:
        print(f"{self.name} ИИТ")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class ICIS(UniversityFactory):
    def activate(self) -> None:
        print(f"{self.name} ИЦИС")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class IPTI(UniversityFactory):
    def activate(self) -> None:
        print(f"{self.name} ИПТИ")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class ISTM(UniversityFactory):
    def activate(self) -> None:
        print(f"{self.name} ИСТМ")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }