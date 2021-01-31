gain = int(input("Enter the gain of your company "))
costs = int(input("Enter the costs of the company "))

if gain > costs:
    profit = gain - costs
    print(f"Good job, your company has profit equal to {profit}!")
    print(f"Your companies profit of proceeds equals to {round((profit / gain) * 100, 2)} per cent!")
    empl = int(input("How many employees does your firm have? "))
    print(f"The firm profit per employee equals to {round(profit / empl, 2)}")
elif costs > gain:
    print("Unfortunately your firm has losses")
elif gain == costs:
    print("There are no profits neither losses")
