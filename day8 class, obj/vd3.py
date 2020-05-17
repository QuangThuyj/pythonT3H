class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f'({self.x1}, {self.y1}, {self.x2}, {self.y2})'

    def getWith(self):
        return abs(self.x2 - self.x1)

    def getHeight(self):
        return abs(self.y2 - self.y1)

    def getArea(self):
        return self.getWith() * self.getHeight()

    def getIntersection(self, rect):
        x1 = max(self.x1, rect.x1)
        x2 = min(self.x2, rect.x2)
        y1 = max(self.y1, rect.y1)
        y2 = min(self.y2, rect.y2)
        if x1 < x2 and y1 < y2:
            return Rect(x1, y1, x2, y2)


r = Rect(1, 2, 5, 6)
print(r.getWith(), r.getHeight(), r.getArea())
r2 = Rect(0, 3, 4, 5)

print(r.getIntersection(r2))