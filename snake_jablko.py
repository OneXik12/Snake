import random
class Jablko():
    def __init__(self):
        self.pozycjaJablka = [(1,1)]
        self.randomPosition()

    def randomPosition(self):
        jablkoX=random.randint(0,19)*30
        jablkoY=random.randint(0,19)*30

#  pobranmie pozycji
    def getPosition(self):
        return self.pozycjaJablka[-1]
# ustawienie pozycji jablka
    def setPosition(self, x, y):
        self.pozycjaJablka(x, y)
