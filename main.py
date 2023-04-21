from pprint import pprint

import aiohttp
import asyncio
from more_itertools import chunked
from function import get_people
from aiohttp import ClientSession
from models import paste_people

from models import Base, SwapiPeople, Session, engine

MAX_REQUESTS = 5


async def main(quantity: int):
    """
    Функция принимает количество персонажей, обрабатывает их циклом range и возвращает список словарей с их данными.

    :param quantity: int
        Количество персонажей, обрабатываемое range.
    :return: list
        Список словарей с данными персонажей.

    """

    # Этот участок кода запускается один раз для создания миграции

    # async with engine.begin() as connection:  # Код создает миграции в БД. Такой код нужен для асинхронного прогр-я.
    #     await connection.run_sync(Base.metadata.create_all)

    async with ClientSession() as client:
        for chunk in chunked(range(1, quantity + 1), MAX_REQUESTS):
            chunk_coro_list = [get_people(people_id=person_id, api_client=client) for person_id in chunk]
            # формируем список корутин.

            res_list = await asyncio.gather(*chunk_coro_list)  # асинхронно обрабатываем список корутин.
            paste_coro = paste_people(res_list)
            paste_task = asyncio.create_task(paste_coro)

    tasks = asyncio.all_tasks() - {asyncio.current_task(), }
    for task in tasks:
        await task


if __name__ == '__main__':
    result = asyncio.run(main(quantity=50))
    # pprint(result[0][0])

