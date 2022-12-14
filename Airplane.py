# Filename: Airplane.py
# Author: Brian Twene
# Date: 9/10/2022

# import abstract method decorator
from abc import ABC, abstractmethod


# class definition
class Airplane(ABC):
    # constructor definition
    def __init__(self, id, destination, initialFuel, model, type):
        # assigning values to instance variables
        self.id = id
        self.destination = destination
        self.fuelTank = initialFuel
        self.model = model
        self.atAirport = True
        self.status = "Idle"
        self.timesFlown = 0
        self.type = type
        self.maintenanceProgress = 0

    # getter functions
    def getType(self):
        return self.type

    def getDestination(self):
        return self.destination

    def getModel(self):
        return self.model

    def getFuelTank(self):
        return self.fuelTank

    def getMaintenanceProgress(self):
        return self.maintenanceProgress

    def getStatus(self):
        return self.status

    # setter methods
    def setType(self, type):

        self.type = type

    def setDestination(self, newDestination):
        self.destination = newDestination

    # add fuel to the plane's fuel tank
    def addFuel(self):
        self.fuelTank += 1

    # empty fuel tank from journey
    def resetFuel(self):
        self.fuelTank = 0

    def resetMaintenance(self):
        self.maintenance = 0
        self.setStatus("Idle")

    def setStatus(self, newStatus):
        if self.status != newStatus:
            self.status = newStatus

    def setTimesFlown(self, times):
        self.timesFlown = times

    # send the plane off
    def setTakeOff(self):
        self.atAirport = False
        self.setStatus("In-Flight")
        self.timesFlown += 1

    # allow the plane to land
    def setLanding(self):
        self.atAirport = True
        self.setStatus("Idle")

    def setMaintenanceProgress(self, progress):
        self.maintenanceProgress = progress

    # doing maintenance checks
    def doMaintenance(self):
        # if the plane has been checked in all 5 areas

        match self.getMaintenanceProgress():
            case 0:
                self.setStatus("Maintenance (1/5): Hydraulics Test")
                self.setMaintenanceProgress(1)
            case 1:
                self.setStatus("Maintenance (2/5): Wheels Test")
                self.setMaintenanceProgress(2)
            case 2:
                self.setStatus("Maintenance (3/5): Brake Test")
                self.setMaintenanceProgress(3)
            case 3:
                self.setStatus("Maintenance (4/5): Plane Body Test")
                self.setMaintenanceProgress(4)
            case 4:
                self.setStatus("Maintenance (5/5): Maintenance Complete")
                self.setMaintenanceProgress(5)
            case 5:
                self.resetMaintenance()

    # abstract methods that will be used in subclasses
    @abstractmethod
    def addEntity(self):
        # adds a passenger or package to the airplane
        pass

    @abstractmethod
    def unload(self):
        pass

    # check for maintenance function
    def checkForMaintenance(self):
        # if plane has flown to and back 3 times
        # send to hangar for maintenance checks
        if self.timesFlown == 3:
            self.setStatus("Maintenance")
            self.setTimesFlown(0)

        else:
            # print(f"Plane {self.id} can fly for {3-self.timesFlown} more time(s)\n")
            self.setStatus("Fueling")
            self.resetFuel()

    # Operator overloading the less than operator for sorting
    def __lt__(self, other):
        self_destination = self.destination["name"]
        other_destination = other.destination["name"]

        return self_destination < other_destination


# subclass for Passenger plane
class PassengerPlane(Airplane):
    # constructor for the class
    # use of super.__init__ to inherit attributes and methods
    def __init__(self, id, destination, initialFuel, model, type):
        super().__init__(id, destination, initialFuel, model, type)

        self.passengers = []

    # function for boarding passengers
    def addEntity(self, Passenger):
        # add new passenger to the plane
        self.passengers.append(Passenger)

    # function for unboarding passengers
    def unload(self):
        self.passengers = []

    # string representation of Passenger Plane
    def __str__(self):

        # passengerList = ""

        # # get the status of all the passengers
        # for index, passenger in enumerate(self.passengers):
        #     passengerList += f"\tPackage {index+1}\n{passenger.__str__()}\n"

        return (
            f"Plane ID: {self.id}\n"
            f"Destination: {self.destination['name']}\n"
            f"Model:{self.model['model']}\n"
            f"Type: {self.type}\n"
            f"Passengers: {len(self.passengers)}\n"
            f"Status: {self.status}\n\n"
            f"List of Passengers\n"
            # f"{passengerList}"
        )


class CargoPlane(Airplane):
    def __init__(self, id, destination, initialFuel, model, type):
        super().__init__(id, destination, initialFuel, model, type)

        self.packages = []

    # overriden function for adding packages
    def addEntity(self, Package):
        # load packages to the plane cabin
        self.packages.append(Package)

    # overriden function for unloading packages
    def unload(self):
        self.packages = []

    # string representation of Cargo Plane
    def __str__(self) -> str:

        # packageList = ""

        # # get the status of all the packages
        # for index, package in enumerate(self.packages):
        #     packageList += f"\tPackage {index+1}\n{package.__str__()}\n"

        return (
            f"Plane ID: {self.id}\n"
            f"Destination: {self.destination['name']}\n"
            f"Model:{self.model['model']}\n"
            f"Type: {self.type}\n"
            f"Packages: {len(self.packages)}\n"
            f"Status: {self.status}\n\n"
            f"List of Packages\n"
            # f"{packageList}"
        )
