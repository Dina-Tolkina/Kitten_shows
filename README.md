# Выставка котят
## Описание
Проект "Выставка котят" представляет собой приложение для управления выставками котят, где пользователи могут регистрироваться, добавлять и оценивать котят. Оно позволяет организаторам выставок управлять породами, котятами и рейтингами, а также обеспечивает администрирование пользователей и прав доступа. Основная задача проекта — упростить процесс регистрации и управления участниками выставок котят.

## Содержание
- [Технологии](#технологии)
- [Как установить и запустить](#как-установить-и-запустить)

## Технологии
- FastAPI — основной фреймворк для создания REST API.
- Tortoise ORM — ORM для работы с базой данных.
- PostgreSQL — база данных для хранения информации о пользователях, котятах, породах и правах доступа.
- Pytest — тестирование с использованием асинхронных тестов.
- HTTPX — клиент для выполнения асинхронных HTTP-запросов.
- Bcrypt — библиотека для хеширования паролей.
- JWT (JSON Web Tokens) — для аутентификации и создания токенов доступа.
- ASGITransport — для передачи запросов внутри тестов через HTTPX.
- Docker и Docker Compose — для контейнеризации и упрощённого развертывания проекта.
- Pydantic — валидация данных и работа со схемами.

## Как установить и запустить
Для начала нужно сделать git clone
  ```sh
  $ git clone https://github.com/Dina-Tolkina/Kitten_shows.git
  ```
Создать venv
  ```sh
  $ python -m venv venv
  ```
Активация виртуальной среды:
- Для Windows:
  ```sh
  $ venv\Scripts\activate
  ```
- Для Unix или MacOS:
  ```sh
  $ source venv/bin/activate
  ```
Установка зависимостей:
  ```sh
  $ pip install -r requirements.txt
  ```
Создать файл .env
  ```sh
  $ POSTGRES_USER=username
    POSTGRES_PASSWORD=password
    POSTGRES_DB=database_name
    DATABASE_URL=postgres://username:password@postgres_db:5432/database_name
    SECRET_KEY=123
    ACCESS_TOKEN_EXPIRE_MINUTES=30
  ```
Сборка и запуск контейнера с помощью docker-compose
  ```sh
  $ docker-compose up --build
  ```
Документация по API будет доступна по адресу:
[http://localhost:8000/docs](http://localhost:8000/docs)

Остановка контейнеров
  ```sh
  docker-compose down
  ```
## Тестирование
В проекте реализованы несколько автоматических тестов, которые проверяют основные функции приложения, такие как создание, обновление, удаление и получение котят. Тесты написаны с использованием pytest и httpx для выполнения асинхронных HTTP-запросов к API.
Запуск тестов
Для запуска тестов выполнить следующую команду:
  ```sh
  pytest
  ```
