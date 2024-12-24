def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 # Handle list with all zeros
    return total / len(numbers)

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,2,0,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zero is: {average_zero}")

my_all_zeros = [0,0,0]
average_all_zeros = calculate_average(my_all_zeros)
print(f"The average of all zeros is: {average_all_zeros}"