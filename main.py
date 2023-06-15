import matplotlib.pyplot as plt

from util import get_data, print_exact_solution, print_results
from methods import methods_list, calculate_x_values, calculate_exact_values

if __name__ == '__main__':
    while True:
        try:
            x_0, x_n, y_0, h, eps, equation = get_data()

            x_values = calculate_x_values(x_0, x_n, h)
            exact_values = calculate_exact_values(equation, x_values, x_0, y_0)
            print_exact_solution(x_values, exact_values)

            plt.grid()
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Решение задачи Коши')
            plt.plot(x_values, exact_values, label='Точное решение')

            for method in methods_list:
                try:
                    y_values = method(equation, x_values, y_0, h, eps)
                    print_results(method.name, x_values, y_values, exact_values, eps)
                    plt.plot(x_values, y_values, marker='o', label=method.name)
                except OverflowError:
                    print(f'\n{method.name} не в состоянии эффективно решить данное ОДУ')

            plt.legend()
            plt.show()

        except (EOFError, KeyboardInterrupt):
            print('\nВыход из программы')
            break
        except ZeroDivisionError:
            print('\nПри вычислениях возникло деление на 0')
            plt.show()
