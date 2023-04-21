from aiohttp import ClientSession


async def get_people(people_id, api_client):
    """
    Функция возвращает json с данными персонажа по запрашиваемому ID.

    :param api_client:
        Сессионный клиент.
    :param people_id: int
        Id персонажа.
    :return: dict
        Json-словарь с данными персонажа.
    """

    url = 'https://swapi.dev/api/people'  # адрес для обращения
    response = await api_client.get(f'{url}/{people_id}/')  # Делаем запрос к API. Т.к. функция асинх. не забываем
    # await, чтобы получить результат работы, а не корутину.

    json_data = await response.json()  # функция асинх, поэтому ставим await и получаем json.
    return json_data
