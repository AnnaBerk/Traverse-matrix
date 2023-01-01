import asyncio
import sys

import aiohttp
from typing import List
import logging

from aiohttp import web
from asyncio import TimeoutError
from aiohttp import ClientError


async def get_string_from_url(url: str) -> str:
    try:
        logging.info('Запрашивает информацию по url')
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if 400 <= response.status < 500:
                    logging.error(response.status)
                    raise web.HTTPNotFound()
                elif 500 <= response.status < 600:
                    logging.error(response.status)
                    raise web.HTTPBadGateway()
                text = await response.text()
                return text
    except TimeoutError as exc:
        logging.error(f"Timeout error {exc}")
    except ClientError as exc:
        logging.error(f"There are problems with connection {exc}")



def format_matrix(matrix_str: str) -> list[list[int]]:
    pass


def traverse_matrix(matrix: list[list[int]]) -> List[int]:
    print(matrix)


async def get_matrix(url: str) -> List[int]:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_string('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main'
    #                                '/matrix.txt'))
    text = await get_string_from_url(url)
    return text


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='main.log',
        filemode='w',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
    )


asyncio.run(
    get_string_from_url('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matri.txt'))