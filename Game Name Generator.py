import random
one = ["Gunner", "Alpha", "Simple", "Lynx", "Psycho", "Mad"]
two = ["Shooter", "Runner", "Simp", "Killer", "Rocker", "Assassin"]
random_name = one + two
print(""" 1. Generate Random name
2. Quit """)

choice = input()
if choice == 1:
    def random_name():
        fn = random.choice(one)
        ln = random.choice(two)
        return f'{fn} {ln}'
    print(random_name)
elif choice == 2:
    print("Bye")