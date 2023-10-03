first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# Use zip_longest from itertools to handle lists with different lengths
from itertools import zip_longest

result_set = set(zip_longest(first_list, second_list))

print(result_set)
