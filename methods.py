from equations import Equation


def calculate_x_values(x_0, x_n, h):
    return [x_0 + i * h for i in range(int((x_n - x_0) / h) + 1)]


def calculate_exact_values(function, x, x_0, y_0):
    return [function.exact(x_i, x_0, y_0) for x_i in x]


class Method:
    name = ''

    def __call__(self, f: Equation, x, y_0, h, eps):
        pass


class Euler(Method):
    name = 'Метод Эйлера'

    def __call__(self, f: Equation, x, y_0, h, eps):
        y = [y_0]
        for i in range(len(x) - 1):
            y.append(y[i] + h * f(x[i], y[i]))
        return y


class ImprovedEuler(Method):
    name = 'Усовершенствованный метод Эйлера'

    def __call__(self, f: Equation, x, y_0, h, eps):
        y = [y_0]
        for i in range(len(x) - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + h, y[i] + h * k1)
            y.append(y[i] + h / 2 * (k1 + k2))
        return y


class Adams(Method):
    name = 'Метод Адамса'

    def __call__(self, f: Equation, x, y_0, h, eps):
        def get_pred():
            return y[i] + h / 24 * (
                    55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3],
                                                                                                         y[i - 3]))

        def get_corr():
            return y[i] + h / 24 * (
                    9 * f(x[i + 1], y_pred) + 19 * f(x[i], y[i]) - 5 * f(x[i - 1], y[i - 1]) + f(x[i - 2], y[i - 2]))

        if len(x) < 4:
            print(f'\n{self.name} не в состоянии решить данное ОДУ')
            return

        y = [y_0]
        for i in range(3):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
            k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
            k4 = f(x[i] + h, y[i] + h * k3)
            y.append(y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

        for i in range(3, len(x) - 1):
            y_pred = get_pred()
            y_cor = get_corr()
            while abs(y_cor - y_pred) > eps:
                y_pred = y_cor
                y_cor = get_corr()
            y.append(y_cor)

        return y


# def adams_old(f: Equation, x, y_0, h):
#     y = [y_0]
#     for i in range(3):
#         k1 = f(x[i], y[i])
#         k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
#         k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
#         k4 = f(x[i] + h, y[i] + h * k3)
#         y.append(y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
#     for i in range(3, len(x) - 1):
#         df = f(x[i], y[i]) - f(x[i - 1], y[i - 1])
#         d2f = f(x[i], y[i]) - 2 * f(x[i - 1], y[i - 1]) + f(x[i - 2], y[i - 2])
#         d3f = f(x[i], y[i]) - 3 * f(x[i - 1], y[i - 1]) + 3 * f(x[i - 2], y[i - 2]) - f(x[i - 3], y[i - 3])
#         y.append(y[i] + h * f(x[i], y[i]) + (h ** 2) * df / 2 + 5 * (h ** 3) * d2f / 12 + 3 * (h ** 4) * d3f / 8)
#     return y


# def process(self, fun, a, b, y0, h, e):
#     dots = [(a, y0)]
#     fun_t = [fun(a, y0)]
#     n = int((b - a) / h) + 1
#
#     for i in range(1, 4):
#         x_prev = dots[i - 1][0]
#         y_prev = dots[i - 1][1]
#         r1 = h * fun(x_prev, y_prev)
#         r2 = h * fun(x_prev + h / 2, y_prev + r1 / 2)
#         r3 = h * fun(x_prev + h / 2, y_prev + r2 / 2)
#         r4 = h * fun(x_prev + h, y_prev + r3)
#
#         x_cur = x_prev + h
#         y_cur = y_prev + (r1 + 2 * r2 + 2 * r3 + r4) / 6
#
#         dots.append((x_cur, y_cur))
#         fun_t.append(fun(x_cur, y_cur))
#
#     # Метод Адамса
#     for i in range(4, n):
#         x_cur = dots[i - 1][0] + h
#
#         y_pred = dots[i - 1][1] + h / 24 * (
#                 55 * fun_t[i - 1] - 59 * fun_t[i - 2] + 37 * fun_t[i - 3] - 9 * fun_t[i - 4])
#
#         fun_t.append(fun(x_cur, y_pred))
#
#         y_cor = dots[i - 1][1] + h / 24 * (9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])
#         while e < abs(y_cor - y_pred):
#             y_pred = y_cor
#             fun_t[i] = fun(x_cur, y_pred)
#             y_cor = dots[i - 1][1] + h / 24 * (
#                     9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])
#
#         dots.append((x_cur, y_cor))
#
#     return dots


methods_list: list[Method] = [
    Euler(),
    ImprovedEuler(),
    Adams()
]
