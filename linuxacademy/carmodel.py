class Car:
    """
    Car model with tires, engine, paint color
    """
    def __init__(self, engine, tires, color):
        self.engine = engine
        self.tires = tires
        self.color = color

    def description(self):

         print(f"A car with an {self.engine} engine, {self.tires} tires and {self.color} color")
    
    def wheel_circumference(self):
        return self.tires.circumference()