from typing import Any

from equations import equations_list, Equation
from util import transpose, table_to_string


def get_data() -> tuple[float, float, float, float, float, Equation]:
    print('\nЧтобы выйти из программы введите exit на любом этапе')

    print_dictionary('ОДУ', equations_list)
    eq_id: int = int(get_value('Выберите уравнение', min_value=1, max_value=len(equations_list), strict=False))
    equation: Equation = equations_list[eq_id]

    x_0: float = get_value('Введите левую границу интервала')
    x_n: float = get_value('Введите правую границу интервала', min_value=x_0)
    y_0: float = get_value('Введите значение y_0')
    h: float = get_value('Введите значение шага h')
    eps: float = get_value('Введите точность')

    return x_0, x_n, y_0, h, eps, equation


def print_results(name: str,
                  x_values: list[float],
                  y_values: list[float],
                  exact_values: list[float],
                  eps: float,
                  table_format: str = 'fancy_grid',
                  float_format: str = '.5f',
                  align: str = 'decimal',
                  show_index: bool = True) -> None:
    y_diff: list[float] = [abs(exact_values[i] - y_values[i]) for i in range(len(y_values))]
    headers: list[str] = ['X', 'Y', 'Y_точное', '|Y - Y_точное|']
    data: list[list[float]] = transpose([x_values, y_values, exact_values, y_diff])

    print(f'\n{name}'
          f'\n{table_to_string(data, headers, table_format, float_format, align, show_index)}')

    y_diff_max: float = max(y_diff)
    if y_diff_max > eps:
        print(f'Точность не достигнута: {y_diff_max:{float_format}} > {eps}')
    else:
        print(f'Точность достигнута: {y_diff_max:{float_format}} <= {eps}')


def print_dictionary(name: str, dictionary: dict[Any, Any]) -> None:
    print(f'\n{name}:', end='')
    for key, value in dictionary.items():
        print(f'\n\t{key}. {value}', end='')
    print()


def get_value(description: str = 'Введите значение',
              min_value: float = float('-inf'),
              max_value: float = float('inf'),
              strict: bool = True,
              invalid_message: str = 'Невалидное значение') -> float:
    value: str = input(f'\n{description}: ').strip().replace(',', '.')

    while not valid_value(value, min_value, max_value, strict):
        print(invalid_message)
        value = input('Повторите ввод: ').strip().replace(',', '.')

    return float(value)


def valid_value(value: str,
                min_value: float = float('-inf'),
                max_value: float = float('inf'),
                strict: bool = True) -> bool:
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        if strict:
            return min_value < float(value) < max_value
        else:
            return min_value <= float(value) <= max_value
    except ValueError:
        return False
