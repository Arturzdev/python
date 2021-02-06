# list
month_num = int(input("Enter month number "))
wint = ['winter', 12, 1, 2]
summer = ['summer', 6, 7, 8]
aut = ['autumn', 9, 10, 11]
spr = ['spring', 3, 4, 5]
if month_num in wint:
    print(wint[0])
if month_num in summer:
    print(summer[0])
if month_num in aut:
    print(aut[0])
if month_num in spr:
    print(spr[0])
# dict
month_number = int(input("Enter month number "))
months = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
          8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}

print(months.get(month_number))
