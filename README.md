# Friends service

## Запуск проекта
- Клонируйте проект с GitHub с помощью команды:
```
git clone https://github.com/Arseniks/friends_service
```
- Перейдите в папку с проектом:
```
cd friends_service
```
### На Windows
- Скопируйте файл .env.template в .env, при необходимости отредактируйте 
  значения переменных:
```
copy .env.template .env
``` 
- Установите и активируйте виртуальное окружение с помощью команд:
```
python -m venv venv
venv\Scripts\activate.bat
``` 
- Установите необходимые вам зависимости

Для основных зависимостей из файла requirements.txt:
```
pip install -r requirements/requirements.txt
``` 
Для разработки нужно также установить зависимости из файла requirements_dev.txt:
```
pip install -r requirements/requirements_dev.txt
``` 
А для тестирования нужно установить зависимости из файла requirements_test.txt:
```
pip install -r requirements/requirements_test.txt
```
- Установки миграций БД:
```
python manage.py migrate
```
- Запуска проекта:
```
python manage.py runserver
```
### На Linux/MAC
- Скопируйте файл .env.template в .env, при необходимости отредактируйте 
  значения переменных:
```
cp .env.template .env
``` 
- Установите и активируйте виртуальное окружение с помощью команд:
```
python3 -m venv venv

source venv/bin/activate
```
- Установите необходимые вам зависимости

Для основных зависимостей из файла requirements.txt:
```
pip3 install -r requirements/requirements.txt
``` 
Для разработки нужно также установить зависимости из файла requirements_dev.txt:
```
pip3 install -r requirements/requirements_dev.txt
```
А для тестирования нужно установить зависимости из файла requirements_test.txt:
```
pip3 install -r requirements/requirements_test.txt
```
- Установки миграций БД:
```
python3 manage.py migrate
``````
- Запуска проекта:
```
python3 manage.py runserver
```