from cs1lib import *
from math import *
from Point import Point


class Dancer:
    def __init__(self, x1, y1, id, state = 0):
        self.positions = [Point(x1, y1)]
        self.state = state


        self.x = self.positions[self.state].x
        self.y = self.positions[self.state].y
        self.id = id
        self.name = "Dancer " + (str) (self.id)
        self.selected = False

        self.color = [1.0, 1.0, 1.0]
        self.radius = 10




    def draw(self):
        set_fill_color(self.color[0], self.color[1], self.color[2])
        draw_circle(self.x, self.y, self.radius)


    def toggleSelect(self):
        self.selected = not self. selected

        if self.selected:
            self.recolor(0,0,1)
            print("here blue")

        else:
            self.recolor()


    def displayName(self):
        set_stroke_color(1, 1,1)
        draw_text(self.name, self.x, self.y + 20)


    def recolor(self, r=1, g=1, b=1):
        self.color=[r,g,b]


    def changeID(self, newId):
        self.id=newId


    def move(self, x, y):
        self.x = x
        self.y = y
        self.positions[self.state].x = x
        self.positions[self.state].y = y


    def newFormation(self, x, y):
        self.positions.append(Point(x,y))


    def transitionTo(self, newPoint):
        speedX = 1
        speedY = 1
        distanceX = abs(self.x - newPoint.x)
        distanceY = abs(self.y - newPoint.y)

        if distanceX > 100:
            speedX = 10
        elif distanceX > 60:
            speedX = 5
        elif distanceX < 15:
            speedX = 1

        if self.x < newPoint.x:
            self.x+=speedX
        elif self.x > newPoint.x:
            self.x -=speedX

        if distanceY > 100:
            speedY = 10
        elif distanceY > 50:
            speedY = 5
        elif distanceY < 10:
            speedY = 1
        if self.y < newPoint.y:
            self.y+=speedY
        elif self.y > newPoint.y:
            self.y -=speedY



    def contains(self, x, y):
        distance = sqrt(((x - self.x) ** 2) + ((y - self.y) ** 2))
        return distance < self.radius + 20


    def changeName(self, newName):
        self.name = newName
