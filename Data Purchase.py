print("""
Welcome to Lancy's Network
Dial *120# to buy data bundles
Dial *150# to check your data balance
Dial *180# to share data to a friend
""")
data_bal = 0

code = input()

if code == "*150#":
    print(f"You currently have {data_bal} MB")

elif code == "*120#":
    print("""1. My Offer
2. Data Bundles
3. Family Plan
4. Social Bundle
""")

choice_1 = input()
if choice_1 == "1":
    print("""
1. N100 for 500MB .. 7 Days
2. N200 for 1GB .. 7 Days
3. N1000 for 5GB .. 7 Days
""")

choice_2 = input()
if choice_2 == "1":
    print("Purchase 500MB for N100")
    print("""
1. Proceed
2. Cancel
""")
    y_or_n = input()
    if y_or_n == "1":
        print("You have successfully purchased 500MB, valid for 7 days")
        data_bal += 500
        print("Your new data balance is : 500MB")
    elif y_or_n == "2":
        print("Canceled")

elif code == "*180#" and data_bal == 0:
    print(f"Dear customer you currently have {data_bal} MB, So you cannot transfer data at the moment ")