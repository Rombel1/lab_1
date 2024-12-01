from classes import (
    UniversityFactory

)
from exceptions import InvalidVehicleTypeException, InvalidFileTypeException
import json
import xml.etree.ElementTree as ET


class VehicleFactory:
    vehicles = {  # Массив разрешённых типов объектов
        "Car": lambda name, capacity: Car(name, capacity),
        "Truck": lambda name, capacity: Truck(name, capacity),
        "Bus": lambda name, capacity: Bus(name, capacity),
        "Bicycle": lambda name, capacity: Bicycle(name, capacity),
        "Motorcycle": lambda name, capacity: Motorcycle(name, capacity),
        "MetroTrain": lambda name, capacity: MetroTrain(name, capacity),
        "Train": lambda name, capacity: Train(name, capacity),
        "Ship": lambda name, capacity: Ship(name, capacity),
        "Plane": lambda name, capacity: Plane(name, capacity),
    }

    @staticmethod
    def create_vehicle(
        vehicle_type, name, capacity
    ):  # Метод для создания объектов классов
        if vehicle_type not in VehicleFactory.vehicles:
            raise InvalidVehicleTypeException(vehicle_type)
        if capacity <= 0:
            raise ValueError(
                f"Неверное значение вместимости: {capacity}. Вместимость должна быть больше 0. "
            )
        return VehicleFactory.vehicles[vehicle_type](name, capacity)

    @staticmethod
    def save_to_json(
        vehicles, filename
    ):  # Метод для сохренения созданных объектов в json
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            with open(filename, "w") as file:
                json.dump([v.to_dict() for v in vehicles], file)

    @staticmethod
    def load_from_json(filename):  # Метод для выгрузки объектов из json
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            with open(filename, "r") as file:
                vehicles_data = json.load(file)
                return [
                    VehicleFactory.create_vehicle(v["type"], v["name"], v["capacity"])
                    for v in vehicles_data
                ]

    @staticmethod
    def save_to_xml(
        vehicles, filename
    ):  # Метод для сохренения созданных объектов в xml
        if ".xml" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            root = ET.Element("Vehicles")
            for vehicle in vehicles:
                vehicle_elem = ET.SubElement(root, "Vehicle")
                type_elem = ET.SubElement(vehicle_elem, "Type")
                name_elem = ET.SubElement(vehicle_elem, "Name")
                capacity_elem = ET.SubElement(vehicle_elem, "Capacity")

                type_elem.text = vehicle.__class__.__name__
                name_elem.text = vehicle.name
                capacity_elem.text = str(vehicle.capacity)

            tree = ET.ElementTree(root)
            tree.write(filename)

    @staticmethod
    def load_from_xml(filename):  # Метод для выгрузки объектов из xml
        if ".xml" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            tree = ET.parse(filename)
            root = tree.getroot()
            vehicles = []

            for vehicle_elem in root.findall("Vehicle"):
                vehicle_type = vehicle_elem.find("Type").text
                name = vehicle_elem.find("Name").text
                capacity = int(vehicle_elem.find("Capacity").text)
                vehicles.append(
                    VehicleFactory.create_vehicle(vehicle_type, name, capacity)
                )

            return vehicles