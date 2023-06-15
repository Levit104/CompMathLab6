from util import get_data, print_results, draw_graph
from methods import methods_list

if __name__ == '__main__':
    while True:
        try:
            x_0, x_n, y_0, h, eps, equation = get_data()

            for method in methods_list:
                x_values, y_values, exact_values = method(equation, x_0, x_n, y_0, h, eps)
                print_results(method.name, x_values, y_values, exact_values, eps)
                draw_graph(method.name, x_values, y_values, exact_values)

        except ZeroDivisionError:
            print('\nВо время вычислений возникло деление на 0')
        except (EOFError, KeyboardInterrupt):
            print('\nВыход из программы')
            break
