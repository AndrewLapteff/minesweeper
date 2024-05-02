class Piece:
    def __init__(self, hasBomb: bool) -> None:
        """
        Ініціалізує об'єкт класу Piece.

        Параметри:
        - hasBomb (bool): Показує, чи містить цей об'єкт бомбу.
        """
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.numAround = 0

    def getHasBomb(self) -> bool:
        """
        Повертає значення, яке показує, чи містить цей об'єкт бомбу.

        Повертає:
        - bool: True, якщо об'єкт містить бомбу, False - якщо ні.
        """
        return self.hasBomb

    def getClicked(self) -> bool:
        """
        Повертає значення, яке показує, чи був клікнутий цей об'єкт.

        Повертає:
        - bool: True, якщо об'єкт був клікнутий, False - якщо ні.
        """
        return self.clicked

    def getFlagged(self) -> bool:
        """
        Повертає значення, яке показує, чи був позначений цей об'єкт прапорцем.
        Повертає:
        - bool: True, якщо об'єкт був позначений прапорцем, False - якщо ні.
        """
        return self.flagged

    def setNeighbors(self, neighbors: list) -> None:
        """
        Встановлює сусідів для цього об'єкта.
        Параметри:
        - neighbors (list): Список об'єктів Piece, які є сусідами цього об'єкта.
        """
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self) -> None:
        """
        Встановлює кількість бомб, які оточують цей об'єкт.
        """
        for piece in self.neighbors:
            if piece.getHasBomb():
                self.numAround += 1

    def getNumAround(self) -> int:
        """
        Повертає кількість бомб, які оточують цей об'єкт.
        Повертає:
        - int: Кількість бомб, які оточують цей об'єкт.
        """
        return self.numAround

    def toggleFlag(self) -> None:
        """
        Змінює стан прапорця для цього об'єкта.
        Якщо прапорець був позначений, то він буде знятий, і навпаки.
        """
        self.flagged = not self.flagged

    def click(self) -> None:
        """
        Встановлює стан клікнутості для цього об'єкта.
        """
        self.clicked = True

    def getNeighbors(self) -> list:
        """
        Повертає сусідів цього об'єкта.
        Повертає:
        - list: Список об'єктів Piece, які є сусідами цього об'єкта.
        """
        return self.neighbors
