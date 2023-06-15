from equations import equations_list
from prettytable import PrettyTable


def valid_value(value, min_value, max_value, strict):
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        if strict:
            return min_value < float(value) < max_value
        else:
            return min_value <= float(value) <= max_value
    except ValueError:
        return False


def get_value(description='Введите значение',
              min_value=float('-inf'), max_value=float('inf'), strict=True,
              invalid_message='Невалидное значение'):
    value = input(f'\n{description}: ').strip().replace(',', '.')

    while not valid_value(value, min_value, max_value, strict):
        print(invalid_message)
        value = input('Повторите ввод: ').strip().replace(',', '.')

    return float(value)


def print_list(name, lst):
    print(f'\n{name}:', end='')
    for index, value in enumerate(lst):
        print(f'\n\t{index + 1}. {value}', end='')
    print()


def print_results(name, x_values, y_values, exact_values, eps):
    y_diff = [abs(exact_values[i] - y_values[i]) for i in range(len(y_values))]

    table = PrettyTable()
    table.add_column('X', x_values)
    table.add_column('Y', y_values)
    table.add_column('Y_точное', exact_values)
    table.add_column('|Y - Y_точное|', y_diff)
    table.float_format = '.5'

    print(f'\n{name}:'
          f'\n{table}')

    y_diff_max = max(y_diff)
    if y_diff_max > eps:
        print(f'Точность не достигнута: {y_diff_max:.5f} > {eps}')
    else:
        print(f'Точность достигнута: {y_diff_max:.5f} <= {eps}')


def print_exact_solution(x_values, exact_values):
    table = PrettyTable()
    table.add_column('X', x_values)
    table.add_column('Y_точное', exact_values)
    table.float_format = '.5'
    print(f'\nТочное решение:'
          f'\n{table}')


def get_data():
    print('\nЧтобы выйти из программы введите exit на любом этапе')

    print_list('ОДУ', equations_list)
    eq_id = int(get_value('Выберите уравнение', min_value=1, max_value=len(equations_list), strict=False))
    equation = equations_list[eq_id - 1]

    x_0 = get_value('Введите левую границу интервала')
    x_n = get_value('Введите правую границу интервала', min_value=x_0)
    y_0 = get_value('Введите значение y_0')
    h = get_value('Введите значение шага h')
    eps = get_value('Введите точность')

    return x_0, x_n, y_0, h, eps, equation
