# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open('text_file.txt', 'w', encoding="utf-8") as txt_f:
    while True:
        user_input = input("Enter your line ")
        if user_input == "":
            break
        else:
            txt_f.write(f"{user_input}\n")
