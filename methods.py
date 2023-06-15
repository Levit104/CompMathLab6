from equations import Equation


class Method:
    name = ''

    @staticmethod
    def calculate_exact(f: Equation, x, x_0, y_0):
        return [f.exact(x_i, x_0, y_0) for x_i in x]

    def calculate(self, f: Equation, x_0, x_n, y_0, h, eps):
        pass

    def __call__(self, f: Equation, x_0, x_n, y_0, h, eps):
        return self.calculate(f, x_0, x_n, y_0, h, eps)


class Euler(Method):
    name = 'Метод Эйлера'

    def calculate(self, f: Equation, x_0, x_n, y_0, h, eps):
        try:
            print(f'{self.name}, h = {h}')
            n = int((x_n - x_0) / h)
            x = [x_0]
            y = [y_0]
            for i in range(n):
                x.append(x[i] + h)
                y.append(y[i] + h * f(x[i], y[i]))
            return x, y, self.calculate_exact(f, x, x_0, y_0)
        except OverflowError:
            return self.calculate(f, x_0, x_n, y_0, h / 2, eps)


class ImprovedEuler(Method):
    name = 'Усовершенствованный метод Эйлера'

    def calculate(self, f: Equation, x_0, x_n, y_0, h, eps):
        try:
            print(f'{self.name}, h = {h}')
            n = int((x_n - x_0) / h)
            x = [x_0]
            y = [y_0]
            for i in range(n):
                k1 = f(x[i], y[i])
                k2 = f(x[i] + h, y[i] + h * k1)
                x.append(x[i] + h)
                y.append(y[i] + h / 2 * (k1 + k2))
            return x, y, self.calculate_exact(f, x, x_0, y_0)
        except OverflowError:
            return self.calculate(f, x_0, x_n, y_0, h / 2, eps)


class Adams(Method):
    name = 'Метод Адамса'

    def calculate(self, f: Equation, x_0, x_n, y_0, h, eps):
        try:
            print(f'{self.name}, h = {h}')

            def get_pred():
                return y[i] + h / 24 * (
                        55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3],
                                                                                                             y[i - 3]))

            def get_corr():
                return y[i] + h / 24 * (
                        9 * f(x[i] + h, y_pred) + 19 * f(x[i], y[i]) - 5 * f(x[i - 1], y[i - 1]) + f(x[i - 2],
                                                                                                     y[i - 2]))

            n = int((x_n - x_0) / h)

            if n + 1 < 4:
                print(f'\n{self.name} не в состоянии решить данное ОДУ, т.к. число узлов меньше 4')
                return

            x = [x_0]
            y = [y_0]
            for i in range(3):
                k1 = f(x[i], y[i])
                k2 = f(x[i] + h / 2, y[i] + h / 2 * k1)
                k3 = f(x[i] + h / 2, y[i] + h / 2 * k2)
                k4 = f(x[i] + h, y[i] + h * k3)
                x.append(x[i] + h)
                y.append(y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

            for i in range(3, n):
                y_pred = get_pred()
                y_cor = get_corr()
                while abs(y_cor - y_pred) > eps:
                    y_pred = y_cor
                    y_cor = get_corr()
                x.append(x[i] + h)
                y.append(y_cor)

            return x, y, self.calculate_exact(f, x, x_0, y_0)
        except OverflowError:
            return self.calculate(f, x_0, x_n, y_0, h / 2, eps)


methods_list: list[Method] = [
    Euler(),
    ImprovedEuler(),
    Adams()
]
