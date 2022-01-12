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

def make_deck(suits):
    deck = []
    for suit in suits:
        for value in range(6, 15):
            card = {}
            card["масть"] = suit
            card["значение"] = value
            deck.append(card)
    random.shuffle(deck)
    return deck


def split_deck(deck):
    user_deck = deck[:18]
    computer_deck = deck[18:]
    return user_deck, computer_deck

deck = make_deck(suits)
user_deck = split_deck(deck)[0]
computer_deck = split_deck(deck)[1]



desk = []
desk.append(user_deck.pop())
desk.append(computer_deck.pop())

print("игрок выбросил", desk[0]["значение"])
print("комьютер выбросил", desk[1]["значение"])


if desk[0]["значение"] > desk[1]["значение"]:
    print("игрок победил")
elif desk[0]["значение"] < desk[1]["значение"]:
    print("комп победил")
else:
    print("спор от ubisoft")
