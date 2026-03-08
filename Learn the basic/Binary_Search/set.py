# Creating a set
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

# Fast membership testing
print(3 in unique_numbers)  # Output: True

# Set operations (Union, Intersection)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}