def my_func(arg_1, arg_2, arg_3):
    a = [arg_1, arg_2, arg_3]
    a.remove(min(a))
    return sum(a)


num_1 = int(input("Enter number 1 "))
num_2 = int(input("Enter number 2 "))
num_3 = int(input("Enter number 3 "))
print(my_func(num_1, num_2, num_3))
