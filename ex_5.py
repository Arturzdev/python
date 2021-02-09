def count(a, b):
    for i in range(len(a)):
        if a[i].isdigit():
            b.append(int(a[i]))
            if i + 1 == len(a):
                print(sum(b))
        elif a[i] == 'Q':
            print(sum(b))
            break
        elif not a[i].isdigit():
            print("You've entered not a number ")
            print(sum(b))


nums = []
while True:
    user_numbers = input("Enter your numbers. If you want to end the program, press 'Q' ").upper().split()
    if 'Q' in user_numbers:
        count(user_numbers, nums)
        break
    else:
        count(user_numbers, nums)
