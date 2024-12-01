class InvalidUniversityTypeException(
    Exception
):  # Исключение возникающее при выборе неверного типа транспорта
    def __init__(self, vehicle_type):
        super().__init__(f"Неверный тип транспорта: {vehicle_type}. ")


class InvalidFileTypeException(
    Exception
):  # Исключение возникающее при выборе неверного типа файла
    def __init__(self, file_type):
        super().__init__(
            f"Неверный тип файла: {file_type}. Допустимые типы: json, xml."
        )