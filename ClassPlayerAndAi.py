from ClassShip import Dot, Ship
from ClassExceptions import BoardException, BoardOutException, BoardUsedException, BoardWrongShipException
from ClassBoard import Board
import random

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy
    # Абстрактный метод, предназначенный для запроса хода у игрока
    def ask(self):
         raise NotImplementedError()
    # Обрабатывает ход игрока. Запрашивает у игрока координаты и обрабатывает выстрел по противнику.
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    # Генерирует случайные координаты для хода компьютера.
    def ask(self):
        d = Dot(random.randint(0,5), random.randint(0,5))
        print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return d

class User(Player):
    # Запрашивает у пользователя координаты для хода.
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()
            
            if len(cords) != 2:
                print("Введите 2 координаты! ")
                continue

            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print("Введите числа! ")
                continue
            
            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)