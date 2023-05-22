# Новостной портал 

## Описание проекта

Новостной сайт, на котором каждый желающий может поделиться новостью

## Технологии

* Python
* Flask
* SQLAlchemy
* WTForms

### Как запустить проект:

Клонировать репозиторий:
```
https://github.com/inovaras/news.git
```

Перейти в него в командной строке:
```
cd flask_news
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создайте файл .env и укажите настройки подключения к БД и другие параметры.

```commandline
SECRET_KEY=YOUR_SECRET_KEY
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
```
Запустить проект:

```
flask run
```



