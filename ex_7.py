# def word_title(a, b):
#     my_list = []
#     for i in range(len(a)):
#         if a[i] in b:
#             my_list.append(a[i])
#             if i + 1 == len(a):
#                 final = (''.join(my_list).title())
#                 print("The sentence is: ", final)
#         elif a[i].isdigit() or a[i] not in b:
#             print("You have to enter only lower case latin letters")
#             break


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#
# user_text = input("Enter your words ").split()
# text = ' '.join(user_text)
#
# word_title(text, letters)

# Я не был уверен, что первая версия программы (выше) соответствует требованию задания, поэтому сделал еще одну.

def word_title(a, b):
    my_list = []
    for i in range(len(a)):
        if a[i] in b:
            my_list.append(a[i])
            if i + 1 == len(a):
                final = (''.join(my_list).title())
                return final
        elif a[i].isdigit() or a[i] not in b:
            print("You have to enter only lower case latin letters")
            break


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_text = input("Enter your words ").split()

text = []
for j in range(len(user_text)):
    text.append(word_title(user_text[j], letters))
    if None in text:
        break
    elif j + 1 == len(user_text):
        text_final = ' '.join(text)
        print("The sentence is: ", text_final)
