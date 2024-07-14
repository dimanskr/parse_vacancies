import json
from abc import ABC, abstractmethod


class CreateStorage(ABC):
    @abstractmethod
    def save(self, storage):
        pass


class ReadStorage(ABC):
    @abstractmethod
    def read_data(self, storage):
        pass


class UpdateStorage(ABC):
    @abstractmethod
    def update_data(self):
        pass


class DeleteStorage(ABC):
    @abstractmethod
    def delete_data(self):
        pass


class JSONHandler(CreateStorage, ReadStorage):

    def __init__(self, objects: list):
        self._objects = objects

    def save(self, file_path):
        """
        Записывает список объектов в файл в формате JSON.`
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([_object.to_dict() for _object in self._objects], f, ensure_ascii=False, indent=4)

    def read_data(self, file_path):
        """
        Получаем список объектов из файла
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            dict_list = json.load(f)

        objects_list = []
        # Создаём объекты из списка словарей загруженных из JSON
        for kwargs in dict_list:
            # type(self._objects[0]) - так мы получаем класс объекта, который передавался списком при инициализации
            # JSONHandler и преобразуем из словарей в объекты
            obj = type(self._objects[0])(**kwargs)
            objects_list.append(obj)
        return objects_list
