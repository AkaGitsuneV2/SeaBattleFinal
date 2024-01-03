# Базовый класс для исключений, связанных с игровой доской.
class BoardException(Exception):
    pass
# Исключение, возникающее при попытке выстрелить за пределы игрового поля.
class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы игрового поля!"
# Исключение, возникающее при попытке повторно выстрелить в уже обстрелянную клетку.
class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку!"
# Исключение, связанное с некорректным размещением корабля на игровой доске.
class BoardWrongShipException(BoardException):
    pass
