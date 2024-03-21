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

experimental_results = []

num_trials_per_n = 10

for n_1 in [2 ** i for i in range(num_trials_per_n)]:
    for n_2 in [2 ** i for i in range(num_trials_per_n)]:
        # create matrix of size n_1 x n_2
        matrix = [[j for j in range(n_2)] for i in range(n_1)]
        find_average_value_rebekah()
        find_average_value_sabrina()
        find_average_value_jason()
        find_average_value_simon()
        find_average_value_evan()
        delta_t = timeit.timeit(lambda: find_average_value(matrix), number=10)

        # append experimental results to running list
        experimental_results.append([n_1, n_2, delta_t])

for i in range(len(experimental_results)):
    if i % num_trials_per_n == 0:
        print()
    print(" ".join([str(item) for item in experimental_results[i]]))
