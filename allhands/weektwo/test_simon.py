import timeit

from typing import List, Union

def find_average_value(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        return None
    matrix_flatmapped: List[int] = []
    for listy in matrix:
        matrix_flatmapped = matrix_flatmapped + listy
    return sum(matrix_flatmapped) / len(matrix_flatmapped)

def time_complexity(n_1: int, n_2: int) -> int:
    return n_1 + 2 * n_1 * n_2 + n_1 * sum([i * n_2 + n_2 for i in range(n_1)])

experimental_results = []
theoretical_results = []

num_trials_per_n = 10

for n_1 in [2 ** i for i in range(num_trials_per_n)]:
    for n_2 in [2 ** i for i in range(num_trials_per_n)]:
        # create matrix of size n_1 x n_2
        matrix = [[j for j in range(n_2)] for i in range(n_1)]
        delta_t = timeit.timeit(lambda: find_average_value(matrix), number=10)

        # append experimental and theoretical results to running list
        experimental_results.append([n_1, n_2, delta_t])
        theoretical_results.append([n_1, n_2, time_complexity(n_1, n_2)])

for i in range(len(experimental_results)):
    if i % num_trials_per_n == 0:
        print()
    print(" ".join([str(item) for item in experimental_results[i]]))

for i in range(len(experimental_results)):
    if i % num_trials_per_n == 0:
        print()
    print(" ".join([str(item) for item in theoretical_results[i]]))
