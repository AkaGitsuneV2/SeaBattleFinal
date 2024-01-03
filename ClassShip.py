from ClassExceptions import BoardException, BoardOutException, BoardUsedException, BoardWrongShipException

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Переопределение метода сравнения для точек.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # Возвращает строковое представление объекта точки.
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    # Параметры:
    # bow (Dot): Точка, обозначающая нос корабля.
    # length (int): Длина корабля.
    # orientation (str): Ориентация корабля ("horizontal" или "vertical").
    def __init__(self, bow, length, orientation):
        self.bow = bow
        self.length = length
        self.orientation = orientation
        self.lives = length
    
    # Возвращает список точек, представляющих корабль на доске.
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y
            
            if self.orientation == "horizontal":
                cur_x += i
            elif self.orientation == "vertical":
                cur_y += i
            
            ship_dots.append(Dot(cur_x, cur_y))
        
        return ship_dots