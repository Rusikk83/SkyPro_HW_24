import os
import json
from flask import Flask, request
from query_job import call_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    try:  # получаем параетры из запроса
        file_name = request.values.get("file_name")
        cmd1 = request.values.get("cmd1")
        value1 = request.values.get("value1")
        cmd2 = request.values.get("cmd2")
        value2 = request.values.get("value2")
    except Exception:
        return "", 400
    path_file = os.path.join(DATA_DIR, file_name)  # формируем пут ьк файлу
    if not os.path.isfile(path_file):  # проверяем наличие файла
        return "", 400

    result1 = call_query(cmd1, value1, path_file, None)  # обработка файла по первой команде
    result2 = call_query(cmd2, value2, path_file, result1)  # обработка данных по второй команде

    return app.response_class(json.dumps(list(result2)), content_type="json")


if __name__ == "__main__":
    app.run()

