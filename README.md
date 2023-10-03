# api_final
## Описание проекта:

Проект позволяет создавать посты и писать комментарии в них.Также имеется возможность чтоб пользователи могли подписываться друг на друга.

## Мой стек технологий:

<img src="https://img.shields.io/badge/Python-FFFAFA?style=for-the-badge&logo=python&logoColor=black"/>

## Как запустить проект: 

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:mirovata/api_final_yatube.git
```
```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
## Некоторые примеры запросов к API:

Запрос на адрес:

```
http://127.0.0.1:8000/api/v1/posts/
```

Позволяет создать пост с необязательным выбором группы и фотографии.

![x](https://github.com/mirovata/api_final_yatube/assets/21317554/8fb51d22-0ef1-449d-83b9-4b06ec5160e9)

Также запрос на адрес:

```
http://127.0.0.1:8000/api/v1/follow/
```

Позволяет пользователям подписаться друг на друга.

![Снимок экрана 2023-10-03 101725](https://github.com/mirovata/api_final_yatube/assets/21317554/1bd21825-7bc0-4fc7-9889-315150dea800)

## Автор:

**Роман Ткаченко** - back-end developer
