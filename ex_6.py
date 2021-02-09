def word_title(a, b):
    my_list = []
    for i in range(len(a)):
        if a[i] in b:
            my_list.append(a[i])
            if i + 1 == len(a):
                temporal = (''.join(my_list).title())
                print("The word is: ", temporal)
        elif a[i].isdigit():
            print("You need to enter only letters")
        elif a[i] not in b:
            print("You have to enter only lower case latin letters")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_text = list(input("Enter your word "))
word_title(user_text, letters)
