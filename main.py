
from UniversityFactory import UniversityFactory
from exceptions import InvalidUniversityTypeException
from classes import University
import json
import xml.etree.ElementTree as ET

# --- UniversityFactory (пример) ---




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
