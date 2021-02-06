my_list = list(input("Insert your numbers "))
el_1 = 0
el_2 = 1
i = 0
last_num = []
if len(my_list) == 0:
    print("You didn't insert any numbers")
if len(my_list) == 1:
    print(my_list)
if " " in my_list:
    while " " in my_list:
        my_list.remove(" ")
if len(my_list) % 2 != 0:
    last_num.append(my_list.pop(-1))
while i < len(my_list):
    my_list[el_1], my_list[el_2] = my_list[el_2], my_list[el_1]
    el_1 += 2
    el_2 += 2
    i += 2
    if i >= len(my_list):
        print(my_list + last_num)
