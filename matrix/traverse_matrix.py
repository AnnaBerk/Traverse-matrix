import asyncio
import aiohttp
from aiohttp import web
from asyncio import TimeoutError
from aiohttp import ClientError
from typing import List
import logging

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
    matrix: list[list[int]] = []
    for line in matrix_str.split('\n'):
        if line and line[0] != '+':
            matrix.append([int(num) for num in line[1:-1].split('|')])
    if matrix and not all([len(matrix) == len(line) for line in matrix]):
        logging.error("Matrix is not squared")
        raise NotSquareMatrix("Matrix is not squared")
    return matrix


def traverse_matrix(matrix: list[list[int]]) -> List[int]:
    mtxlen: int = len(matrix)
    rowlen: int = len(matrix)
    result: list[int] = []
    row: int = 0
    col: int = 0

    while row < mtxlen and col < rowlen:
        for i in range(rowlen):
            result.append(matrix[i][row])

        row += 1

        for i in range(row, mtxlen, 1):
            result.append(matrix[rowlen - 1][i])

        rowlen -= 1

        if row < mtxlen:
            for i in range(rowlen - 1, col - 1, -1):
                result.append(matrix[i][mtxlen - 1])

            mtxlen -= 1

        if col < rowlen:
            for i in range(mtxlen - 1, row, -1):
                result.append(matrix[col][i])

            col += 1

    return result


def get_matrix(url: str) -> List[int]:
    text = asyncio.run(get_string_from_url(url))
    return traverse_matrix(format_matrix(text))


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='main.log',
        filemode='w',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
    )

get_matrix('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt')
