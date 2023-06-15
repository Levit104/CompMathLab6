from math import exp, sqrt, log


class Equation:
    def exact(self, x, x_0, y_0):
        pass

    def __call__(self, x, y):
        pass


class Equation1(Equation):
    def exact(self, x, x_0, y_0):
        return -exp(x) / (x * exp(x) - (exp(x_0) + x_0 * y_0 * exp(x_0)) / y_0)

    def __call__(self, x, y):
        return y + (1 + x) * y ** 2

    def __str__(self):
        return 'y` = y + (1 + x) * y^2'


class Equation2(Equation):
    def exact(self, x, x_0, y_0):
        return -2 / (x ** 2 - (2 / y_0 - x_0 ** 2))

    def __call__(self, x, y):
        return x * y ** 2

    def __str__(self):
        return 'y` = x * y^2'


class Equation3(Equation):
    def exact(self, x, x_0, y_0):
        return log(x + sqrt(x ** 2 - 1)) + y_0 - log(x_0 + sqrt(x_0 ** 2 - 1))

    def __call__(self, x, y):
        return 1 / (sqrt(x ** 2 - 1))

    def __str__(self):
        return 'y` = 1/sqrt(x^2 - 1)'


equations_list = [
    Equation1(),
    Equation2(),
    Equation3()
]
