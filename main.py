import json
from UniversityFactory import UniversityFactory
from exceptions import InvalidUniversityTypeException
import xml.etree.ElementTree as ET



# --- Определения классов университетов ---
class University:
    def __init__(self, type, name, year):
        self.type = type
        self.name = name
        self.year = year

    def info(self):
        return f"Тип: {self.type}, Название: {self.name}, Год создания: {self.year}"

# --- UniversityFactory (пример) ---
class UniversityFactory:
    @staticmethod
    def create_University(type, name, year):
        if type == "СТАНКИН":
            return University("СТАНКИН", name, year)
        elif type == "МГИМО":
            return University("МГИМО", name, year)
        elif type == "МГУ":
            return University("МГУ", name, year)
        elif type == "ИТМО":
            return University("ИТМО", name, year)
        elif type == "СПБГУ":
            return University("СПБГУ", name, year)
        else:
            raise InvalidUniversityTypeException(f"Неизвестный тип университета: {type}")

    @staticmethod
    def save_to_json(universities, filename):
        data = [vars(u) for u in universities]  # Преобразуем объекты в словари
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [University(**u) for u in data] # Создаем объекты из словарей


    @staticmethod
    def save_to_xml(universities, filename):
        root = ET.Element("Universities")
        for university in universities:
            uni_element = ET.SubElement(root, "University")
            ET.SubElement(uni_element, "type").text = university.type
            ET.SubElement(uni_element, "name").text = university.name
            ET.SubElement(uni_element, "year").text = str(university.year)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)


    @staticmethod
    def load_from_xml(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        universities = []
        for uni_element in root.findall('University'):
            type = uni_element.find('type').text
            name = uni_element.find('name').text
            year = int(uni_element.find('year').text)
            universities.append(University(type, name, year))
        return universities



# --- exceptions.py (пример) ---
class InvalidUniversityTypeException(Exception):
    pass


def display_menu():
    print("1. Добавить университет")
    print("2. Сохранить университет в файл json")
    print("3. Загрузить университет из файла json")
    print("4. Сохранить университет в файл xml")
    print("5. Загрузить университет из файла xml")
    print("6. Вывести на экран университеты")
    print("0. Выход")


def main():
    universities = []

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            university_type = input(
                "Введите тип университета (СТАНКИН, МГИМО, МГУ, ИТМО, СПБГУ.): "
            )
            model = input("Введите название университета: ")
            capacity = int(input("Введите год создания: "))
            try:
                university = UniversityFactory.create_University(university_type, model, capacity)
                universities.append(university)
                print("Университет добавлен!")
            except InvalidUniversityTypeException as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            filename = input(
                "Введите название файла для сохранения университетов (напр.: universities.json): "
            )
            UniversityFactory.save_to_json(universities, filename)
            print(f"Университеты сохранены в {filename}")

        elif choice == "3":
            filename = input(
                "Введите название файла для загрузки университетов (напр.: universities.json): "
            )
            try:
                loaded_universities = UniversityFactory.load_from_json(filename)
                universities.extend(loaded_universities)
                print(
                    f"Загружено {len(loaded_universities)} университетов из {filename}"
                )
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Ошибка загрузки университетов: {e}")

        elif choice == "4":
            filename = input(
                "Введите название файла для сохранения университетов (напр.: universities.xml): "
            )
            UniversityFactory.save_to_xml(universities, filename)
            print(f"Университеты сохранены в {filename}")

        elif choice == "5":
            filename = input(
                "Введите название файла для загрузки университетов (напр.: universities.xml): "
            )
            try:
                loaded_universities = UniversityFactory.load_from_xml(filename)
                universities.extend(loaded_universities)
                print(
                    f"Загружено {len(loaded_universities)} университетов из {filename}"
                )
            except (FileNotFoundError, ET.ParseError) as e:
                print(f"Ошибка загрузки университетов: {e}")

        elif choice == "6":
            print("Университеты:")
            for university in universities:
                print(university.info())

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
