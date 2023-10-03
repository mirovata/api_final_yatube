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

[![x.png](https://i.postimg.cc/xdpCNZq0/x.png)](https://postimg.cc/NyTYWp1V)

Также запрос на адрес:

```
http://127.0.0.1:8000/api/v1/follow/
```

Позволяет пользователям подписаться друг на друга.

[![dasdas.png](https://i.postimg.cc/9f7SyRQr/dasdas.png)](https://postimg.cc/t192jgPj)

## Автор:

**Роман Ткаченко** - back-end developer
