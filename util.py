from typing import Any

from tabulate import tabulate
from matplotlib import pyplot as plt


def draw_graph(name: str, x_values: list[float], y_values: list[float], exact_values: list[float]) -> None:
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Решение задачи Коши')
    plt.plot(x_values, exact_values, label='Точное решение')
    plt.plot(x_values, y_values, marker='o', label=name)
    plt.legend()
    plt.show()


def transpose(table: list[list[Any]]) -> list[list[Any]]:
    return [list(row) for row in zip(*table)]


def table_to_string(data: list[Any],
                    headers: list[Any],
                    table_format: str = 'fancy_grid',
                    float_format: str = '.5f',
                    align: str = 'decimal',
                    show_index: bool = True) -> str:
    table: str = tabulate(data,
                          headers=headers,
                          tablefmt=table_format,
                          floatfmt=float_format,
                          numalign=align,
                          showindex=show_index)
    return table
