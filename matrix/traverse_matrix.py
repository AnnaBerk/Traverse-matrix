import asyncio
import sys

import aiohttp
from typing import List
import logging

from aiohttp import web
from asyncio import TimeoutError
from aiohttp import ClientError

from matrix.exceptions import NotSquareMatrix


async def get_string_from_url(url: str) -> str:
    try:
        logging.info('Getting url')
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if 400 <= response.status < 500:
                    logging.error(response.status)
                    raise web.HTTPNotFound()
                elif 500 <= response.status < 600:
                    logging.error(response.status)
                    raise web.HTTPBadGateway()
                return await response.text()
    except TimeoutError as exc:
        logging.error(f"Timeout error {exc}")
    except ClientError as exc:
        logging.error(f"There are problems with connection {exc}")


def format_matrix(matrix_str: str) -> list[list[int]]:
    logging.info('Formatting matrix')
    matrix = []
    for line in matrix_str.split('\n'):
        if line and line[0] != '+':
            matrix.append([int(num) for num in line[1:-1].split('|')])
    if matrix and not all([len(matrix) == len(line) for line in matrix]):
        logging.error("Matrix is not squared")
        raise NotSquareMatrix("Matrix is not squared")
    return matrix

def traverse_matrix(matrix: list[list[int]]) -> List[int]:
    print(matrix)


def get_matrix(url: str) -> List[int]:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_string('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main'
    #                                '/matrix.txt'))
    text = asyncio.run(get_string_from_url(url))
    format_matrix(text)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='main.log',
        filemode='w',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
    )

get_matrix('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt')

# m = '+-----+-----+-----+-----+\n| 20 | 20 |  30 |  40 |\n+-----+-----+-----+-----+\n|  50 |  60 |  70 |  80 |\n+-----+-----+-----+-----+\n|  90 | 100 | 110 | 120 |\n+-----+-----+-----+-----+\n| 130 | 140 | 150 | 160 |\n+-----+-----+-----+-----+\n'
# format_matrix(m)
