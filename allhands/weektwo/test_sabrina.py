# Insert solutions here

from typing import List, Union
import time

# Rebekah Solution 
def rebekah_find_average_value(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not matrix:
        return None
    total_numbers = []
    for number_list in matrix:
        for number in number_list:
            total_numbers.append(number)
    return sum(total_numbers) / len(total_numbers)

# Sabrina Solution
def sabrina_find_average_value(matrix: List[List[int]]) -> Union[float, None]:
    """Find the average value in the provided matrix."""
    if not matrix or not all(
        isinstance(row, list) and all(isinstance(val, int) for val in row)
        for row in matrix
    ):
        return None
    total_sum = sum(sum(row) for row in matrix)
    num_elements = sum(len(row) for row in matrix)
    return total_sum / num_elements

# Function for execution time
def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Example matrices (Used Chat GPT to create examples)
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[1, 2, 3], [4, 5, 'a'], [7, 8, 9]]  # Invalid matrix for Sabrina's function

# Calculate execution time for the first function
execution_time_1 = calculate_execution_time(rebekah_find_average_value, matrix_1)
print("🎉Execution time for Rebekah's Solution🎉", execution_time_1, "seconds")
# Calculate execution time for the second function
execution_time_2 = calculate_execution_time(sabrina_find_average_value, matrix_1)
print("🎉Execution time for Sabrina's solution:🎉", execution_time_2, "seconds")
