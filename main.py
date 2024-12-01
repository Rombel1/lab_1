import json
from UniversityFactory import UniversityFactory
from exceptions import InvalidUniversityTypeException
import xml.etree.ElementTree as ET


def display_menu():
    print("1. Добавить факультет университета")
    print("2. Сохранить факультет в файл json")
    print("3. Загрузить факультет из файла json")
    print("4. Сохранить факультет в файл xml")
    print("5. Загрузить факультет из файла xml")
    print("6. Вывести на экран текущие тфакультеты")
    print("0. Выход")


def main():
    UniversityFactory = []

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            UniversityFactory_type = input(
                "Введите Факультет (ИИТ, ИЦИС, ИПТИ, ИСТМ): "
            )
            model = input("Введите название Факультета: ")
            capacity = int(input("Введите специальность: "))
            try:
                UniversityFactory = UniversityFactory.create_vehicle(UniversityFactory_type, model, capacity)
                UniversityFactory.append(UniversityFactory)
                print("Факультет добавлен!")
            except InvalidUniversityTypeException as e:
                print(f"Error: {e}")

        elif choice == "2":
            filename = input(
                "Введите название файла для сохранения факультета (напр.: UniversityFactory.json): "
            )
            UniversityFactory.save_to_json(UniversityFactory, filename)
            print(f"Факультет сохренён в {filename}")

        elif choice == "3":
            filename = input(
                "Введите название файла из которого загрузить факультет (напр.: UniversityFactory.json): "
            )
            try:
                UniversityFactory = UniversityFactory.load_from_json(filename)
                UniversityFactory.extend(loaded_vehicles)
                print(
                    f"Загружено {len(loaded_vehicles)} Факультет из {filename}"
                )
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading UniversityFactory: {e}")

        elif choice == "4":
            filename = input(
                "Введите название файла для сохранения Факультета (напр.: UniversityFactory.xml): "
            )
            UniversityFactory.save_to_xml(UniversityFactory, filename)
            print(f"Транспорт сохранён в {filename}")

        elif choice == "5":
            filename = input(
                "Введите название файла из которого загрузить Факултет (напр.: UniversityFactory.xml): "
            )
            try:
                loaded_vehicles = UniversityFactory.load_from_xml(filename)
                UniversityFactory.extend(loaded_vehicles)
                print(
                    f"Загружено {len(UniversityFactory)} Факультет из {filename}"
                )
            except (FileNotFoundError, ET.ParseError) as e:
                print(f"Ошибка при загрузке факультета: {e}")

        elif choice == "6":
            print("факультет:")
            for UniversityFactory in UniversityFactory:
                print(UniversityFactory.info())

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз")


if __name__ == "__main__":
    main()