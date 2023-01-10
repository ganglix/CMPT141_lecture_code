import random

options = ["cash", "buzzer"]
total_lis = []


def draw_cash():
    cash_drawn = random.randint(50, 200)
    return cash_drawn


for i in range(20):
    while True:
        print(f"\nround {i + 1}/20")
        call = input("go? Y or N: ").upper()
        if call in ["Y", "N"]:
            break
        else:
            print("please type only Y or N \n")
    if call == "Y":
        choice = (random.choices(options, weights=(80, 20)))[0]
        if choice == "cash":
            cash = draw_cash()
            total_lis.append(cash)
            print(f"${cash}")
            print(f"total:${sum(total_lis)}")

        if choice == "buzzer":
            print("buzzer! You got nothing")
            print(f"You could have got:${sum(total_lis)}")
            break
    else:
        print(f"total:${sum(total_lis)}")
        break
