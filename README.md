# api_final
Описание проекта:

Проект предоставляет API с возможностью создавать посты,комментарии и делать подписки на людей.

Как запустить проект: 

Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:mirovata/api_final_yatube.git

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver

Некоторые примеры запросов к API:

После запуска проекта вы можете обратиться к документации проекта по адресу:

http://127.0.0.1:8000/redoc/

Там описаны все примеры обращений к сервису и его ответы
