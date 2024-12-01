from classes import (
    UniversityFactory, IIT, ICIS, IPTI, ISTM

)
from exceptions import InvalidUniversityTypeException, InvalidFileTypeException
import json
import xml.etree.ElementTree as ET


class VehicleFactory:
    University = {  # Массив разрешённых типов объектов
        "IIT": lambda name, capacity: IIT(name, capacity),
        "ICIS": lambda name, capacity: ICIS(name, capacity),
        "IPTI": lambda name, capacity: IPTI(name, capacity),
        "ISTM": lambda name, capacity: ISTM(name, capacity),

    }

    @staticmethod
    def create_vehicle(
        University_type, name, capacity
    ):  # Метод для создания объектов классов
        if University_type not in UniversityFactory.University:
            raise InvalidUniversityTypeException(University_type)
        if capacity <= 0:
            raise ValueError(
                f"Неверное значение вместимости: {capacity}. Вместимость должна быть больше 0. "
            )
        return UniversityFactory.University[University_type](name, capacity)

    @staticmethod
    def save_to_json(
        University, filename
    ):  # Метод для сохренения созданных объектов в json
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            with open(filename, "w") as file:
                json.dump([v.to_dict() for v in University], file)

    @staticmethod
    def load_from_json(filename):  # Метод для выгрузки объектов из json
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            with open(filename, "r") as file:
                University_data = json.load(file)
                return [
                    UniversityFactory.create_University(v["type"], v["name"], v["capacity"])
                    for v in University_data
                ]

    @staticmethod
    def save_to_xml(
        University, filename
    ):  # Метод для сохренения созданных объектов в xml
        if ".xml" not in filename:
            raise InvalidFileTypeException(filename)
        else:
            root = ET.Element("University")
            for University in University:
                vehicle_elem = ET.SubElement(root, "Vehicle")
                type_elem = ET.SubElement(vehicle_elem, "Type")
                name_elem = ET.SubElement(vehicle_elem, "Name")
                capacity_elem = ET.SubElement(vehicle_elem, "Capacity")

                type_elem.text = University.__class__.__name__
                name_elem.text = University.name
                capacity_elem.text = str(University.capacity)

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

            for University_elem in root.findall("University"):
                vehicle_type = University_elem.find("Type").text
                name = University_elem.find("Name").text
                capacity = int(University_elem.find("Capacity").text)
                UniversityFactory.append(
                    UniversityFactory.create_University(UniversityFactory, name, capacity)
                )

            return UniversityFactory