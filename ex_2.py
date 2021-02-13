first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([el for i, el in enumerate(first_list) if i != 0 and el > first_list[i - 1]])
