my_list = [7, 5, 3, 3, 2]
item = int(input('Enter number '))
if item > my_list[0]:
    my_list.insert(0, item)
if item < my_list[(-1)]:
    my_list.append(item)
for i in my_list:
    if item == i:
        my_list.insert(my_list.index(i), item)
        print(my_list)
        break
