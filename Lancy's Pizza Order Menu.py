print("..............Welcome To Lancy's Pizza..............")
print("..........This are our available size options below..........")
print("1 - Small     :     $10")
print("2 - Medium    :     $15")
print("3 - Large     :     $27")
print("What size do you want")
size = input()
if size == "1":
    print("You choosed the small size")
    print("Now choose your topping")
    print("1 - Chicken")
    print("2 - Pepperoni")
    print("3 - Suya")
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
    else :
        print("That option is not available.....Order Cancelled")

elif size == "2":
            print("You choosed the medium size")
            print("Now choose your topping")
            print("1 - Chicken")
            print("2 - Pepperoni")
            print("3 - Suya")
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
            else:
                print("That option is not available.....Order Cancelled")

elif size == "3":
            print("You choosed the large size")
            print("Now choose your topping")
            print("1 - Chicken")
            print("2 - Pepperoni")
            print("3 - Suya")
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
                print("THANK YOU FOR CHOOSING LANCY'S PIZZA HAHA")
                receipt = input("Would you like to print receipt: ")
            else:
                print("That option is not available.....Order Cancelled")
else:
    print("That option is not available.....Order Cancelled")