def pars(**kwargs):
    print(f"The parameters are: ", kwargs.values())


name = input("Enter your name ").title()
sur_name = input("Enter your surname ").title()
b_year = int(input("Enter your year of birth "))
city = input("Enter your home city ").title()
mail = input("Enter your mail address ")
if "@" not in mail:
    while "@" not in mail:
        print("That's not a mail address ")
        mail = input("Enter your mail address ")

phone = int(input("Enter your phone number "))

pars(name=name, surname=sur_name, birthyear=b_year,
     city=city, mail=mail, phone=phone)
