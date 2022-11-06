# Filename: Airplane.py
# Author: Brian Twene
# Date: 9/10/2022

# import abstract method decorator
from abc import ABC, abstractmethod


# class definition
class Airplane(ABC):
    # constructor definition
    def __init__(self, id, destination, initialFuel, model):
        # assigning values to instance variables
        self.id = id
        self.destination = destination
        self.fuelTank = initialFuel
        self.model = model
        self.atAirport = True
        self.status = "idle"
        self.timesFlown = 0

    # getter functions
    def getDestination(self):
        return self.destination

    def getModel(self):
        return self.model

    def getFuelTank(self):
        return self.fuelTank

    # setter methods
    def setDestination(self, newDestination):
        self.destination = newDestination

    # add fuel to the plane's fuel tank
    def fuel(self, fuel):
        self.fuelTank += fuel

    # empty fuel tank from journey
    def resetFuel(self):
        self.fuelTank = 0

    def setStatus(self, newStatus):
        if self.status != newStatus:
            self.status = newStatus

    # abstract methods that will be used in subclasses
    @abstractmethod
    def addEntity(self):
        # adds a passenger or package to the airplane
        pass

    @abstractmethod
    def unload(self):
        pass

    # send the plane off
    def takeOff(self):
        self.atAirport = False
        self.setStatus("In-Flight")
        self.timesFlown += 1

    # allow the plane to land
    def land(self):
        self.atAirport = True
        self.setStatus("idle")
        self.resetFuel()

    # check for maintenance function
    def checkForMaintenance(self):
        # if plane has flown to and back 3 times
        # send to hangar for maintenance checks
        if self.timesFlown == 3:
            self.setStatus("Maintenance")
        else:
            print(f"plane can fly for {3-self.timesFlown} more time(s)")
            self.setStatus("Fueling")
            self.resetFuel()


# subclass for Passenger plane
class PassengerPlane(Airplane):
    # constructor for the class
    # use of super.__init__ to inherit attributes and methods
    def __init__(self, id, destination, initialFuel, model):
        super().__init__(id, destination, initialFuel, model)

        self.passengers = []
        self.type = "Passenger"

    # function for boarding passengers
    def addEntity(self, Passenger):
        # add new passenger to the plane
        self.passengers.append(Passenger)

    # function for unboarding passengers
    def unload(self):
        self.passengers = []

    # string representation of Passenger Plane
    def __str__(self):

        passengerList = ""

        # get the status of all the passengers
        for index, passenger in enumerate(self.passengers):
            passengerList += f"\tPackage {index+1}\n{passenger.__str__()}\n"

        return (
            f"Plane ID: {self.id}\n"
            f"Destination: {self.destination['name']}\n"
            f"Model:{self.model['model']}\n"
            f"Type: {self.type}\n"
            f"Passengers: {len(self.passengers)}\n"
            f"Status: {self.status}\n\n"
            f"List of Passengers\n"
            f"{passengerList}"
        )


class CargoPlane(Airplane):
    def __init__(self, id, destination, initialFuel, model):
        super().__init__(id, destination, initialFuel, model)

        self.packages = []
        self.type = "Cargo"

    # overriden function for adding packages
    def addEntity(self, Package):
        # load packages to the plane cabin
        self.packages.append(Package)

    # overriden function for unloading packages
    def unload(self):
        self.packages = []

    # string representation of Cargo Plane
    def __str__(self) -> str:

        packageList = ""

        # get the status of all the packages
        for index, package in enumerate(self.packages):
            packageList += f"\tPackage {index+1}\n{package.__str__()}\n"

        return (
            f"Plane ID: {self.id}\n"
            f"Destination: {self.destination['name']}\n"
            f"Model:{self.model['model']}\n"
            f"Type: {self.type}\n"
            f"Packages: {len(self.packages)}\n"
            f"Status: {self.status}\n\n"
            f"List of Packages\n"
            f"{packageList}"
        )
