def count(a, b):
    if not (a.replace('.', '').isdigit()) or not (b.lstrip('-').isdigit()):
        print("You need to enter numbers")
    elif a.replace('.', '').isdigit() and b.lstrip('-').isdigit():
        temporary_1 = float(a)
        temporary_2 = int(b)
        if isinstance(temporary_1, float) and temporary_2 < 0:
            print(temporary_1 ** temporary_2)
        elif not (isinstance(temporary_1, float)) or not (temporary_2 < 0):
            print("Number one has to be float and number two negative")


num_1 = input("Enter first number ")
num_2 = input("Enter second number, has to be negative ")

count(num_1, num_2)
