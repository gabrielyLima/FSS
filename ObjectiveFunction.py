import math
import numpy as np

class ObjectiveFunction(object):
    def __init__(self, name, dim, minf, maxf):
        self.function_name = name
        self.dim = dim
        self.minf = minf
        self.maxf = maxf

    def evaluate(self, x):
        pass


class SphereFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(SphereFunction, self).__init__('Sphere', dim, -100.0, 100.0)

    def evaluate(self, x):
        return np.sum(x ** 2)


class RosenbrockFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(RosenbrockFunction, self).__init__('Rosenbrock', dim, -30.0, 30.0)

    def evaluate(self, x):
        sum_ = 0.0
        for i in range(1, len(x) - 1):
            sum_ += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
        return sum_


class RastriginFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(RastriginFunction, self).__init__('Rastrigin', dim, -5.12, 5.12)

    def evaluate(self, x):
        f_x = [xi ** 2 - 10 * math.cos(2 * math.pi * xi) + 10 for xi in x]
        return sum(f_x)

