# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_file_4.txt', 'r', encoding="utf-8") as txt_f_4, open('text3.txt', 'w', encoding="utf-8") as txt_fill:
    my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
    my_str = str()
    for line in txt_f_4:
        line = line.split()
        for item in my_dict.items():
            if line[0] == item[0]:
                line[0] = item[1]
                my_str = " ".join(line)
                txt_fill.writelines(my_str + '\n')
