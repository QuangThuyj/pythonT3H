class Robot:
    def __init__(self, x, y):
        self.moveUp = x + 1
        self.moveDown = x - 1
        self.moveLeft = y - 1
        self.moveRight = y + 1
    def posion(self, x, y):
        self.x = x
        self.y = y



