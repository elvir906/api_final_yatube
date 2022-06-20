### Описание проекта:

Проект API_YATUBE_FINAL призван использовать возможности API для проекта YATUBE (социальная сеть, позволяющая регистрироваться в нём и создавать посты с текстами и изображениями). API позволяет взаимодейстовать проекту с различными ПО для извлечения, добавления и редактирования контента, представленного в проекте, посредством запросов.

### Установка. Как развернуть проект на локальной машине

```
git clone https://github.com/elvir906/api_yatube_final.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Некоторые примеры запросов к API

получение всех постов, содержащихся в проекте, GET-запросом. POST-запрос на этот же эндпоинт создаст новый пост.
```
http://127.0.0.1:8000/api/v1/posts/
```
пример результата запроса
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2021-10-14T20:41:29.648Z",
"image": "string",
"group": 0
}
]
}
```

получение поста по его id методом GET
```
http://127.0.0.1:8000/api/v1/posts/{id}/
{
"text": "string",
"image": "string",
"group": 0
}
```

GET и POST запрос на этот эндпоинт выдаст список всех комментариев поста по его id и создаст новый к этому посту, соответственно
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

получение комментария, размещенных под постом методом GET, по id поста и id комментария
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

GET-запрос на этот эндпоинт возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. POST-запрос создаст подписку на пользователя, переданного в теле запроса
```
http://127.0.0.1:8000/api/v1/follow/

{
"user": "string",
"following": "string"
}
```
