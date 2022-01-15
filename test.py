import random

"""игра в пьяницу
   
   создать колоду из 36 карт:
   4 масти
   9 значений
       коллекция из карт
       карта: масть + значение
    
    перемешать колоду

    раздача:
     карты игрока - 1/2 от колоды
     карты соперника - 1/2 от колоды
    
    начать раунд:
     взять верхнюю карту игрока и положить на стол
     взять верхнюю карту бота и положить на стол
     
    сравниваем карты на столе:
     вариант значение игрока больше соперника
         игрок забирает стол (снизу)
     вариант значение соперника больше игрока
         противник забтрает стол (снизу)
     вариант значение соперника = игрока
         выбросить еще пару и сравнить вновь
    победа и проигрыш: 
        кончилилсь карты
        нечем ответить в споре

    
"""
suits = ("червей", "пик", "кресте", "бубен")

def make_deck():
    deck = []
    for suit in suits:
        for value in range(6, 15):
            card = {}
            card["масть"] = suit
            card["значение"] = value
            deck.append(card)
    random.shuffle(deck)
    return deck


def split_deck():
    user_deck = deck[:18]
    computer_deck = deck[18:]
    return user_deck, computer_deck

deck = make_deck()
user_deck = split_deck()[0]
computer_deck = split_deck()[1]



table = []

def new_game():
    while len(user_deck) > 0:
        table.append(user_deck.pop())
        table.append(computer_deck.pop())

        print("игрок выбросил", table[0]["значение"])
        print("комьютер выбросил", table[1]["значение"])

        if table[0]["значение"] > table[1]["значение"]:
            print("игрок победил")
            user_deck.reverse()
            user_deck.append(table)
            user_deck.reverse()
            print(len(user_deck))
            input("--------------------")
        elif table[0]["значение"] < table[1]["значение"]:
            print("комп победил")
            computer_deck.reverse()
            computer_deck.append(table)
            computer_deck.reverse()
            print(len(computer_deck))
            input("-----------------------")
        else:
            print("спор")
            input("-------------------")
            new_game()



make_deck()
split_deck()
new_game()

