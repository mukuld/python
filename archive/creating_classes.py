class Car:
    """
    The class Car creates a car with engine, tires and color
    """

    def __init__(self, engine, tires, color):
        self.engine = engine
        self.tires = tires
        self.color = color

    def description(self):
        print(f"A car with an {self.engine} engine, {self.tires} tires and {self.color} color")

