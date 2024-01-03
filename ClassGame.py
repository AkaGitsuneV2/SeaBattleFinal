from ClassShip import Dot, Ship
from ClassExceptions import BoardException, BoardOutException, BoardUsedException, BoardWrongShipException
from ClassBoard import Board
from ClassPlayerAndAi import Player, AI, User
import random

class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(random.randint(0, self.size), random.randint(0, self.size)), l, random.choice(['horizontal', 'vertical']))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board
    
    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветствуем вас  ")
        print("      в игре        ")
        print("    'Морской бой'   ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-"*20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-"*20)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1
            
            if self.ai.board.count == 7:
                print("-"*20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-"*20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()