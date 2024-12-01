import json
from UniversityFactory import UniversityFactory
from exceptions import InvalidVehicleTypeException
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
    vehicles = []

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            vehicle_type = input(
                "Введите тип транспорта (Car, Bus, Bicycle, Plane, Truck, Ship, Train, MetroTrain, Motorcycle.): "
            )
            model = input("Введите название транспорта: ")
            capacity = int(input("Введите вместимость: "))
            try:
                vehicle = VehicleFactory.create_vehicle(vehicle_type, model, capacity)
                vehicles.append(vehicle)
                print("Транспорт добавлен!")
            except InvalidVehicleTypeException as e:
                print(f"Error: {e}")

        elif choice == "2":
            filename = input(
                "Введите название файла для сохранения транспорта (напр.: vehicles.json): "
            )
            VehicleFactory.save_to_json(vehicles, filename)
            print(f"Транспорт сохренён в {filename}")

        elif choice == "3":
            filename = input(
                "Введите название файла из которого загрузить транспорт (напр.: vehicles.json): "
            )
            try:
                loaded_vehicles = VehicleFactory.load_from_json(filename)
                vehicles.extend(loaded_vehicles)
                print(
                    f"Загружено {len(loaded_vehicles)} Транспортных средств из {filename}"
                )
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading vehicles: {e}")

        elif choice == "4":
            filename = input(
                "Введите название файла для сохранения транспорта (напр.: vehicles.xml): "
            )
            VehicleFactory.save_to_xml(vehicles, filename)
            print(f"Транспорт сохранён в {filename}")

        elif choice == "5":
            filename = input(
                "Введите название файла из которого загрузить транспорт (напр.: vehicles.xml): "
            )
            try:
                loaded_vehicles = VehicleFactory.load_from_xml(filename)
                vehicles.extend(loaded_vehicles)
                print(
                    f"Загружено {len(loaded_vehicles)} Транспортных средств из {filename}"
                )
            except (FileNotFoundError, ET.ParseError) as e:
                print(f"Ошибка при загрузке транспорта: {e}")

        elif choice == "6":
            print("Транспорт:")
            for vehicle in vehicles:
                print(vehicle.info())

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз")


if __name__ == "__main__":
    main()