import math

class Tire:
    """
    Tire represents a tire that would be used with an automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand="", construction="R"):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction
    
    def circumference(self):
        """
        The circumference of tire in inches

        >>> tire = Tire("P", 215, 75, 18)
        >>> tire.circumference()
        96.4
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches * 2) + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        """
        Represent the tire's information in standard notation present on the
        sidewall of the tire. Example: "P215/65R18"
        """
        return f"{self.tire_type}{self.width}/{self.ratio}{self.construction}{self.diameter}"
    
    def _side_wall_inches(self):
        return (self.width * (self.ratio/100)) / 25.4

class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand="", construction="R"):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        Circumference of a tire with snow chains in inches
        
        >>> tire = SnowTire("P", 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """

        side_wall_inches = self._side_wall_inches()
        total_diameter = ((side_wall_inches + self.chain_thickness) * 2) + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (Snow)"