import numpy as np

class SearchSpaceInitializer(object):

    def sample(self, objective_function, n):
        pass


class UniformSSInitializer(SearchSpaceInitializer):

    def sample(self, objective_function, n):
        x = np.zeros((n, objective_function.dim))
        for i in range(n):
            x[i] = np.random.uniform(objective_function.minf, objective_function.maxf, objective_function.dim)
        return x

