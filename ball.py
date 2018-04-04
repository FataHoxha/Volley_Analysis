from random import randint
import time


class VolleyBall:
    tracks = []

    def __init__(self, i, xi, yi, max_age,frame):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.state = '0'
        self.age = 0
        self.max_age = max_age
        self.frame =frame

    def getTracks(self):
        return self.tracks

    def getId(self):
        return self.i

    def getState(self):
        return self.state

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getFrame(self):
        return self.frame

    def updateCoords(self, xn, yn,frame):
        self.age = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn
        self.frame=frame



