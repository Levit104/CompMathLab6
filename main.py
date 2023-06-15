import matplotlib.pyplot as plt

from util import get_data, print_results
from methods import methods_list

if __name__ == '__main__':
    while True:
        try:
            x_0, x_n, y_0, h, eps, equation = get_data()

            for method in methods_list:
                plt.grid()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Решение задачи Коши')
                x_values, y_values, exact_values = method(equation, x_0, x_n, y_0, h, eps)
                print_results(method.name, x_values, y_values, exact_values, eps)
                plt.plot(x_values, exact_values, label='Точное решение')
                plt.plot(x_values, y_values, marker='o', label=method.name)
                plt.legend()
                plt.show()

        except ZeroDivisionError:
            print('\nВо время вычислений возникло деление на 0')
        except (EOFError, KeyboardInterrupt):
            print('\nВыход из программы')
            break
