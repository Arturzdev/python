my_list = [57, 'hello', 34.67, True, ['world', 88], 9, (5, 4), ([4, 3, 'Hi'])]
i = 0
while i <= len(my_list):
    print(type(my_list[i]))
    i += 1
    if i == len(my_list):
        break
