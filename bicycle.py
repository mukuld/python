# Python Programme Number 93
# Class Generation: Inheritance
# Programmer: Mukul Dharwadkar
# Date: 30 July 2010

import cPickle, shelve

class Bicycle(object):
    """A bicycle creating class"""
    total = 0
    def __init__(self, name, cadence=0, speed=0, gear=1):
        print "A new bicycle is manufactured."
        self.name = name
        print "Its name is:", self.name
        self.cadence = cadence
        print "Its cadence is:", self.cadence
        self.speed = speed
        print "Its speed is:", self.speed
        self.gear = gear
        print "Its gear is:", self.gear
        Bicycle.total += 1
    
    def chg_cadence(self, cadence):
        self.cadence = cadence
        
    def inc_speed(self, speedup):
        self.speed = speed + speedup
        
    def dec_speed(self, brake):
        self.speed = speed - brake
        
    def chg_gear(self, gear):
        self.gear = gear
        
    def total_bikes():
        print "You currently have", Bicycle.total, "bicycle(s)"
    
    total_bikes = staticmethod(total_bikes)
    def print_state(self):
        print "The current state of your bike is given below"
        print "The name of your bike is:", self.name
        print "The cadence is:", self.cadence
        print "The speed is:", self.speed
        print "The gear is:", self.gear
        
def bike_factory():
    name = raw_input("What would like to name your bike? ")
    cadence = input("What should be the cadence? ")
    speed = input("What should be the speed ")
    gear = input("What gear should be it in? ")
    bike = Bicycle(name, cadence, speed, gear)
    dump_data(bike)
    return bike

def dump_data(self):
    file = open("bikes.dat", "w")
    cPickle.dump(bike(), file)
    file.close()
    
def main():
#    Bicycle.total_bikes()
#   bike1 = Bicycle(50, 18, 4)
    choice = None
    while choice != 0:
        print \
            """
            Bike Factory
            0 - Exit
            1 - Make a bike
            2 - unDump Data
            3 - Change speed
            4 - Change gear
            """ 
        
        choice = input("What would you like to do? ")
        
        if choice == 0:
            print "Good-bye"
        elif choice == 1:
            bike_factory()
        elif choice == 2:
            dump_data()
            
#    bike_factory()
    Bicycle.total_bikes()
#    bike1.chg_cadence(60)
#    bike1.print_state()
#    Bicycle.total_bikes()
main()