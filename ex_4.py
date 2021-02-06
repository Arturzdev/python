def convert(lst):
    return [i for item in lst for i in item.split()]


words = input('Enter words ')
word_list = convert([words])
for ind, el in enumerate(word_list, 1):
    print(ind, el[:10:])
