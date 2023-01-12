print("..............Welcome To Lancy's Pizza..............")
print("..........This are our available size options below..........")
print("1 - Small     :     $10")
print("2 - Medium    :     $15")
print("3 - Large     :     $27")
print("What size do you want")
size = input()

while size < "1" or size > "3":
    print(f"Option '{size}' is not valid")
    print("Please, pick from the available options")
    size = input()

# small pizza (starts)
if size == "1":
    print("You selected the small size")
    print("Now choose your topping")
    print("1 - Chicken")
    print("2 - Pepperoni")
    print("3 - Suya")
    topping = input()

    while topping < "1" or topping > "3":
        print(f"Option '{topping}' is not valid")
        print("Please, pick from the available options")
        topping = input()

    if topping == "1":
        print("You selected the chicken topping, yummy!")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 10
        print("========YOUR BILL========")
        print("Size       : Small")
        print("Topping    : Chicken")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "2":
        print("You selected the pepperoni topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 10
        print("========YOUR BILL========")
        print("Size       : Small")
        print("Topping    : Pepperoni")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "3":
        print("You selected the suya topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 10
        print("========YOUR BILL========")
        print("Size       : Small")
        print("Topping    : Suya")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")
# small pizza (ends)

# medium pizza (starts)
elif size == "2":
    print("You selected the medium size")
    print("Now choose your topping")
    print("1 - Chicken")
    print("2 - Pepperoni")
    print("3 - Suya")
    topping = input()

    while topping < "1" or topping > "3":
        print(f"Option '{topping}' is not valid")
        print("Please, pick from the available options")
        topping = input()

    if topping == "1":
        print("You selected the chicken topping, yummy!")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 15
        print("========YOUR BILL========")
        print("Size       : Medium")
        print("Topping    : Chicken")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "2":
        print("You selected the pepperoni topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 15
        print("========YOUR BILL========")
        print("Size       : Medium")
        print("Topping    : Pepperoni")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "3":
        print("You selected the suya topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 15
        print("========YOUR BILL========")
        print("Size       : Medium")
        print("Topping    : Suya")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")
# medium pizza (ends)

# large pizza (starts)
elif size == "3":
    print("You selected the large size")
    print("Now choose your topping")
    print("1 - Chicken")
    print("2 - Pepperoni")
    print("3 - Suya")
    topping = input()

    while topping < "1" or topping > "3":
        print(f"Option '{topping}' is not valid")
        print("Please, pick from the available options")
        topping = input()

    if topping == "1":
        print("You selected the chicken topping, yummy!")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 27
        print("========YOUR BILL========")
        print("Size       : Large")
        print("Topping    : Chicken")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "2":
        print("You selected the pepperoni topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 27
        print("========YOUR BILL========")
        print("Size       : Large")
        print("Topping    : Pepperoni")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")

    elif topping == "3":
        print("You selected the suya topping")
        print("How many pcs do you need? ")
        pcs = int(input())
        final = pcs * 27
        print("========YOUR BILL========")
        print("Size       : Large")
        print("Topping    : Suya")
        print("Price      : $" + str(final))
        print("THANK YOU FOR CHOOSING LANCY'S PIZZA")
# large pizza (ends)