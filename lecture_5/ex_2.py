# Создать текстовый файл (не программно), сохранить в нём
# несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open('text_file_2.txt', 'r', encoding="utf-8") as txt_f_2:
    lines = 0
    words = 0
    for line in txt_f_2:
        lines += 1
        words += len(line.split())
print(lines)
print(words)
