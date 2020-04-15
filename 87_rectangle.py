# Python Programme Number 87
# Magic Methods: Rectangle, accessing properties
# Programmer: Mukul Dharwadkar
# Date: 11 June 2009

class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)
