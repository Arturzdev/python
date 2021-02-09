def divide(num_1, num_2):
    if num_2 == 0:
        print("You can't divide on 0, try another number ")
    else:
        return num_1 / num_2


n_1 = int(input('Enter the first number '))
n_2 = int(input('Enter the second number '))

print(divide(n_1, n_2))
