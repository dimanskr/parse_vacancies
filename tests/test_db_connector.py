# Тест для метода save
import json

from src.db_connector import JSONHandler


def test_save_json(list_objects, tmpdir):
    file_path = tmpdir.join('test.json')
    handler = JSONHandler(list_objects)
    handler.save(str(file_path))

    assert file_path.exists()

    # Проверяем содержимое файла
    with open(str(file_path), 'r', encoding='utf-8') as f:
        saved_data = json.load(f)

    assert len(saved_data) == len(list_objects)
    assert all(obj.to_dict() in saved_data for obj in list_objects)


# Тест для метода read_data
def test_read_data(list_objects, tmpdir):
    file_path = tmpdir.join('test.json')

    # Записываем данные в файл
    with open(str(file_path), 'w', encoding='utf-8') as f:
        json.dump([obj.to_dict() for obj in list_objects], f, ensure_ascii=False)

    handler = JSONHandler(list_objects)
    loaded_objects = handler.read_data(str(file_path))

    assert len(loaded_objects) == len(list_objects)
    assert all(isinstance(obj, type(list_objects[0])) for obj in loaded_objects)
