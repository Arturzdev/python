def num_fact(num):
    num_f = 1
    if num == 0:
        yield '1'
    for i in range(1, num + 1):
        num_f *= i
        yield num_f


for el in num_fact(int(input("Enter your number "))):
    print(el)
