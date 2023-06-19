from io_handler import get_data, print_results
from util import draw_graph
from methods import methods_list

if __name__ == '__main__':
    while True:
        try:
            float_format = '.5f'
            x_0, x_n, y_0, h, eps, equation = get_data()

            for method in methods_list:
                try:
                    x_values, y_values, exact_values = method(equation, x_0, x_n, y_0, h, eps)
                    print_results(method.name, x_values, y_values, exact_values, eps,
                                  float_format=float_format,
                                  align='center')
                    draw_graph(method.name, x_values, y_values, exact_values)
                except (ZeroDivisionError, ValueError) as e:
                    print(f'\n{method.name} не в состоянии решить данное ОДУ: {e}')

        except (EOFError, KeyboardInterrupt):
            print('\nВыход из программы')
            break
