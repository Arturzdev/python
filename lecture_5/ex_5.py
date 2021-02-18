# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("text_file_5.txt", "w", encoding="utf-8") as txt_f_5:
    nums = [randint(1, 100) for _ in range(100)]
    txt_f_5.write(" ".join(map(str, nums)))

print(f"Sum of elements - {sum(nums)}")
