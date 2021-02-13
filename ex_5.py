from functools import reduce

print(reduce(lambda a, b: a * b, [c for c in range(100, 1001, 2)]))
