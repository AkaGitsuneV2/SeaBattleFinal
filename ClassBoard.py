from ClassShip import Dot, Ship
from ClassExceptions import BoardException, BoardOutException, BoardUsedException, BoardWrongShipException

class Board:
    # Инициализирует объект доски с указанным размером и настройками видимости.
    def __init__(self, hid = False, size=6):
        self.size = size
        self.hid = hid
        self.count = 0

        self.field = [["O"]*size for _ in range(size)]
        self.busy = []
        self.ships = []
    # Добавляет корабль на доску.
    def add_ship(self,ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)
        self.ships.append(ship)
        self.contour(ship)
    # Отмечает окружающую область вокруг корабля на доске
    def contour(self,ship,verb = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)
    # Возвращает строковое представление доски для отображения.
    def __str__(self):
        res = ""
        res += " | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res
    # Проверяет, находится ли координата вне границ доски.
    def out(self, d):
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))
    # Обрабатывает выстрел в указанной координате на доске.
    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "T"
        print("Мимо!")
        return False
    # Инициализирует игру, сбрасывая список занятых координат.
    def begin(self):
        self.busy = []
