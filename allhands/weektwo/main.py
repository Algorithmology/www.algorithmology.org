import timeit
from typing import List, Union

## Rebekah Rudd Solution

def find_average_value_rebekah(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    # check to see if matrix is populated
    if not matrix:
        return None
    # create an empty list
    total_numbers = []
    # iterate through matrix and extract all the numbers to find the min
    for number_list in matrix:
        for number in number_list:
            total_numbers.append(number)
    # return the minimum value within the total_numbers list using min()
    return sum(total_numbers) / len(total_numbers)

## Sabrina Rodriguez Solution

def find_average_value_sabrina(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not matrix or not all(
        isinstance(row, list) and all(isinstance(val, int) for val in row)
        for row in matrix
    ):
        return None
    total_sum = sum(sum(row) for row in matrix)
    num_elements = sum(len(row) for row in matrix)
    return total_sum / num_elements

## Jason Gyamfi Solution

def find_average_value_jason(matrix):
    """Find the average value in the provided matrix."""
    if not matrix:
        return None
    total = sum(sum(row) for row in matrix)
    count = sum(len(row) for row in matrix)
    return total / count

## Simon Jones Solution

def find_average_value_simon(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        return None
    matrix_flatmapped: List[int] = []
    for listy in matrix:
        matrix_flatmapped = matrix_flatmapped + listy
    return sum(matrix_flatmapped) / len(matrix_flatmapped)

## Evan Nelson Solution

def find_average_value_evan(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if (
        not matrix
        or not all(isinstance(row, list) for row in matrix)
        or any(not row for row in matrix)
    ):
        return None
    flattened_matrix = [element for row in matrix for element in row]
    average = sum(flattened_matrix) / len(flattened_matrix)
    return average

experimental_results_rebekah = []
experimental_results_sabrina = []
experimental_results_jason = []
experimental_results_simon = []
experimental_results_evan = []

num_trials_per_n = 10

for n_1 in [2 ** i for i in range(num_trials_per_n)]:
    for n_2 in [2 ** i for i in range(num_trials_per_n)]:
        # create matrix of size n_1 x n_2
        matrix = [[j for j in range(n_2)] for i in range(n_1)]
        delta_t_rebekah = timeit.timeit(lambda: find_average_value_rebekah(matrix), number=10)
        delta_t_sabrina = timeit.timeit(lambda: find_average_value_sabrina(matrix), number=10)
        delta_t_jason = timeit.timeit(lambda: find_average_value_jason(matrix), number=10)
        delta_t_simon = timeit.timeit(lambda: find_average_value_simon(matrix), number=10)
        delta_t_evan = timeit.timeit(lambda: find_average_value_evan(matrix), number=10)

        # append experimental results to running list
        experimental_results_rebekah.append([n_1, n_2, delta_t_rebekah])
        experimental_results_sabrina.append([n_1, n_2, delta_t_sabrina])
        experimental_results_jason.append([n_1, n_2, delta_t_jason])
        experimental_results_simon.append([n_1, n_2, delta_t_simon])
        experimental_results_evan.append([n_1, n_2, delta_t_evan])


def average_doubling_ratio(l: List[float]) -> float:
    """Get doubling ratio for given list of floats"""
    doubling_ratios = []
    print(l)
    for i in range(num_trials_per_n - 1):
        doubling_ratios.append(l[i+1] / l[i])
    return sum(doubling_ratios) / len(doubling_ratios)

def print_doubling_ratios(results):
    for i in range(int(len(results) / num_trials_per_n)):
        print("Holding n_1 constant:")
        print(average_doubling_ratio([item[2] for item in results[i*num_trials_per_n:(i+1)*num_trials_per_n]]))
    for i in range(num_trials_per_n):
        print("Holding n_2 constant:")
        list_to_compute = []
        for j in range(int(len(results) / num_trials_per_n)):
            list_to_compute.append(results[i + j])
        print(average_doubling_ratio([item[2] for item in list_to_compute]))

print("----- Rebekah results ------")
print_doubling_ratios(experimental_results_rebekah)
for i in range(len(experimental_results_rebekah)):
    print(" ".join([str(item) for item in experimental_results_rebekah[i]]))

print()
print("----- Sabrina results ------")
print_doubling_ratios(experimental_results_sabrina)
for i in range(len(experimental_results_sabrina)):
    print(" ".join([str(item) for item in experimental_results_sabrina[i]]))

print()
print("----- Jason results ------")
print_doubling_ratios(experimental_results_jason)
for i in range(len(experimental_results_jason)):
    print(" ".join([str(item) for item in experimental_results_jason[i]]))

print()
print("----- Simon results ------")
print_doubling_ratios(experimental_results_simon)
for i in range(len(experimental_results_simon)):
    print(" ".join([str(item) for item in experimental_results_simon[i]]))

print()
print("----- Evan results ------")
print_doubling_ratios(experimental_results_evan)
for i in range(len(experimental_results_evan)):
    print(" ".join([str(item) for item in experimental_results_evan[i]]))
