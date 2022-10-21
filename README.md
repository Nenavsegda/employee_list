# Подразделения с древовидной структурой и списком сотрудников

## Стек
<ul>Python</ul>
<ul>Django</ul>
<ul>Bootstrap</ul>
<ul>JS</ul>

## Описание

 Веб страница, которая будет выводить древовидную структуру отделов со списком сотрудников.

* Информация о каждом сотруднике храниться в базе данных  и содержать следующие данные
1. [x] ФИО;
2. [x] Должность;
3. [x] Дата приема на работу;
4. [x] Размер заработной платы;
5. [x] Подразделение - подразделения имеют структуру до 5 уровней;


* Дерево отображается в свернутом виде.

* Для создания базовых стилей страницы был использован Twitter Bootstrap.


## Разворачивание на машине разработчика

* Клонируем [employee_list](https://github.com/Nenavsegda/employee_list).
* Переходим в директорию employee_list и устанавливаем виртуальное окружение:

```bash
cd employee_list && sudo apt install python3-venv
```

* Создаем окружения для игры

```bash
python3 -m venv employee_list-env
```

* Активируем виртуальное окружение

```bash
 source employee_list/bin/activate
```
* Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

* Подключаем базу данных в докер:

```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=root -e POSTGRES_DB=employee_list -p 5432:5432 -d postgres
```

* Запускаем миграции и наполняем базу данных. Нужно дождаться завершения команда, "Сотрудники сохранены"

```bash
python manage.py migrate
python manage.py populatedb
```

* После завершения команды, можно запускать сервер. Веб-страница будет по адресу http://127.0.0.1:8000/

```bash
python manage.py runserver
```