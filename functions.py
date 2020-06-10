numbers_1_to_100 = range(1, 101)

for num in numbers_1_to_100:
    if num % 5 == 0 and num % 7 == 0:
        print("ChickenMonkey")
    elif num % 7 == 0:
        print("Monkey")
    elif num % 5 == 0:
        print("Chicken")
    else:
        print(num)

print()


def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool!")


run("Pam", "Sam", "Andrea", "Will")

print()


def swing(*kids):
    for kid in kids:
        print(f"{kid} swung on the swing set")


swing("Marybeth", "Ariel", "Kevin", "Courtney")

print()


def slide(*kids):
    for kid in kids:
        print(f"{kid} slid down the hill")


slide("Mike", "Jack", "Jennifer", "Earl")

print()


def hide(*kids):
    for kid in kids:
        print(f"{kid} hid from the other kids")


hide("Henry", "Heather", "Hayley", "Hugh")

print()


def calc_dollars(**coins):
    totalCents = 0
    for key, value in coins.items():
        if key == "pennies":
            totalCents += value
        elif key == "nickels":
            totalCents += (value * 5)
        elif key == "dimes":
            totalCents += (value * 10)
        elif key == "quarters":
            totalCents += (value * 25)
    dollarAmount = totalCents/100
    print(f"${dollarAmount}")


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)

print()

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def calc_coins(cash):
    while (cash > 0):
        if cash/.25 >= 1:
            piggyBank["quarters"] = int(cash // .25)
            cash -= cash // .25 * .25
            cash = round(cash, 2)
        if cash/.1 >= 1:
            piggyBank["dimes"] = int(cash // .1)
            cash -= cash // .1 * .1
            cash = round(cash, 2)
        if cash/.05 >= 1:
            piggyBank["nickels"] = int(cash // .05)
            cash -= cash // .05 * 0.05
            cash = round(cash, 2)
        if cash/.01 >= 1:
            piggyBank["pennies"] = int(cash // .01)
            cash -= cash // .01 * 0.01


calc_coins(dollarAmount)

print(piggyBank)
