from itertools import count, cycle

for i in count(int(input("Enter starting number "))):
    print(i, end='')
    stop = input()
    if stop == 's':
        break

user_list = input("Enter your numbers ").split()
next_list = cycle(user_list)
finish = None

while finish != 'f':
    print(next(next_list), end='')
    finish = input()
