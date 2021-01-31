n = input("Enter your number ")
i = 1
n_len = len(n)
max_num = n[0]
while i <= n_len:
    if i == n_len:
        print(max_num)
        break
    elif n[i] <= max_num:
        i += 1
    elif max_num <= n[i]:
        max_num = n[i]
        i += 1
