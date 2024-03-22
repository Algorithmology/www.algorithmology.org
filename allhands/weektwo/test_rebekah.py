# Insert solutions here

from typing import List, Union
import time

def rebekah_find_average_value(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not matrix:
        return None
    total_numbers = []
    for number_list in matrix:
        for number in number_list:
            total_numbers.append(number)
    return sum(total_numbers) / len(total_numbers)

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

execution_time_1 = calculate_execution_time(rebekah_find_average_value, matrix_1)
print("🎉Execution time for Rebekah's Solution🎉", execution_time_1, "seconds")