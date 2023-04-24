# Домашнее задание к лекции «Asyncio»

Программа по получению персонажей звездных войн и внесения их в базу.

* СУБД - PostgreSQL.
* Перед работой нужно создать БД, данные для подключения внести в файл .env, образец можно взять из файла .env.example.
* Внести в код нужное количество запросов.
* Запустить run. Программа сама создаст таблицу в БД и наполнит ее. При повторном запуске программа удалит старую таблицу, после создаст новую и наполнит ее. 