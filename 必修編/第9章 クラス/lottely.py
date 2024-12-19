from random import choice

possibilities = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"{pulled_item}を引きました")
        winning_ticket.append(pulled_item)

print(f"当選番号は{winning_ticket}です！")