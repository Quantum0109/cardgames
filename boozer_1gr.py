import random
import os

suits = ("червей", "пик", "крестей", "бубен")
values = range(6, 15)


def populate_deck(deck, suits, values):
    for suit in suits:
        for value in values:
            card = {}
            card["масть"] = suit
            card["значение"] = value
            deck.append(card)
    random.shuffle(deck)


def deal(deck, user_deck, computer_deck):
    for card in deck[:len(deck) // 2]:
        user_deck.append(card)
    for card in deck[len(deck) // 2:]:
        computer_deck.append(card)


def new_game():
    deck = []
    user_deck = []
    computer_deck = []
    table = []

    populate_deck(deck, suits, values)
    deal(deck, user_deck, computer_deck)

    while user_deck and computer_deck:
        new_round(user_deck, computer_deck, table)
    
    print("--- результат игры: ---")
    if user_deck:
        print("победил игрок")
    else:
        print("победил компьютер")


def new_round(user_deck, computer_deck, table):
    # печатаем карты
    os.system("cls")
    print("\n----- карты игрока: -----")
    for card in user_deck:
        print(f'{card["значение"]} {card["масть"]}, ', end="")
    print("\n\n----- карты компьютера: -----")
    for card in computer_deck:
        print(f'{card["значение"]} {card["масть"]}, ', end="")

    # выбрасываем карты на стол
    user_card = user_deck.pop()
    computer_card = computer_deck.pop()
    table.append(user_card)
    table.append(computer_card)

    # печатаем выброшенные карты
    print("\n\n----- ход игрока -----")
    print(user_card["значение"], user_card["масть"])

    print("\n----- ход компьютера -----")
    print(computer_card["значение"], computer_card["масть"])

    # спор
    while user_card["значение"] == computer_card["значение"]:
        user_card = user_deck.pop()
        computer_card = computer_deck.pop()

        table.append(user_card)
        table.append(computer_card)

        # печатаем выброшенные карты
        print("\n\n----- ход игрока в споре -----")
        print(user_card["значение"], user_card["масть"])
        print("\n----- ход компьютера в споре -----")
        print(computer_card["значение"], computer_card["масть"]) 

    # определяем, чья карта больше
    print("\n----- результат раунда: -----")
    if user_card["значение"] == 6 and computer_card["значение"] == 14:
        print("игрок победил и забирает карты:")
        for card in table:
            user_deck.insert(0, card)
            print(f'{card["значение"]} {card["масть"]}, ', end="")

    elif computer_card["значение"] == 6 and user_card["значение"] == 14:
        print("компьютер победил и забирает карты:")
        for card in table:
            computer_deck.insert(0, card)
            print(f'{card["значение"]} {card["масть"]}, ', end="")

    else: #нормальный подсчёт
        if user_card["значение"] > computer_card["значение"]:
            print("игрок победил и забирает карты:")
            for card in table:
                user_deck.insert(0, card)
                print(f'{card["значение"]} {card["масть"]}, ', end="")
        else:
            print("компьютер победил и забирает карты:")
            for card in table:
                computer_deck.insert(0, card)
                print(f'{card["значение"]} {card["масть"]}, ', end="")

    table.clear()
    input("\n\nENTER - продолжить")


new_game()
