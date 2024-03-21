# Insert solutions here

from typing import List, Union
import time

def find_average_value(matrix: List[List[int]]) -> Union[float, None]:
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

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

execution_time_1 = calculate_execution_time(find_average_value, matrix_1)
print("🎉Execution time for Evan's Solution🎉", execution_time_1, "seconds")
