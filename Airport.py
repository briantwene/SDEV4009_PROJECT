# Filename: Airport.py
# Author: Brian Twene
# Date: 9/10/2022

# import modules and classes for use
import random
from Airplane import PassengerPlane, CargoPlane
from cargo import Cargo
from AppExecption import AirportException

from util import createTable, generateDestination

# Airport class definition
class Airport:

    # constructor method for passing the name of the airport
    def __init__(self, name="Dublin Airport"):
        self.planes = []
        self.name = name
        self.showFeed = False

    # setter methods
    # add a plane to the airport
    def addPlane(self, Plane):
        self.planes.append(Plane)

    def setShowFeed(self, feed):
        self.showFeed = feed

    # fuel a plane that is in the airport
    def fuelPlane(self):

        # check for planes that are not in flight
        availablePlanes = list(filter(lambda x: x.atAirport, self.planes))

        # if there is a plane
        if availablePlanes:

            # select a plane and get its fuel tank status
            Plane = random.choice(availablePlanes)
            cost = Plane.destination["cost"]
            currentFuel = Plane.getFuelTank()

            # check if the fuel is enough for the journey
            # if not
            if currentFuel < cost:
                # then add the remainder of fuel
                Plane.addFuel()
                if self.showFeed:
                    print(
                        f"Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} added fuel, current tank = {Plane.fuelTank}/{cost} ⛽\n"
                    )
            # otherwise set the plane to On-Boarding status
            else:
                if self.showFeed:
                    print(
                        f"Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} Fueling finished, setting status to On-Boarding\n"
                    )
                Plane.setStatus("On-Boarding")
        # if there are no planes at the airport

    # function for loading passengers and cargo
    def onLoad(self, entity):

        # first check if the entity is cargo
        # if it is then
        if isinstance(entity, Cargo):

            # find cargo planes that are avaliable
            availablePlanes = list(
                filter(
                    lambda x: isinstance(x, CargoPlane) and x.status == "On-Boarding",
                    self.planes,
                )
            )

            # and if there is..
            if availablePlanes:

                # select a plane from what is available
                Plane = random.choice(availablePlanes)

                # get the current weight of the items that are in the plane
                currentWeight = sum(package.weight for package in Plane.packages)

                # check if the weight has reached max capacity
                # if not
                if currentWeight < Plane.model["maxCargoWeight"]:
                    # then add the package
                    Plane.addEntity(entity)
                    if self.showFeed:
                        print(
                            f"Package, {entity.name} has been added to Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} 📦\n"
                        )

                # otherwise set the plane to the next stage as it is full
                else:
                    if self.showFeed:
                        print(
                            f"Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} loading Cargo finished. setting status to Ready ✅\n"
                        )
                    Plane.setStatus("Ready")
        # if not a cargo package then its a passenger
        else:

            # now find the avaliable passenger planes
            availablePlanes = list(
                filter(
                    lambda x: isinstance(x, PassengerPlane)
                    and x.status == "On-Boarding",
                    self.planes,
                )
            )

            # if there are any..
            if availablePlanes:

                # select from them
                Plane = random.choice(availablePlanes)

                # and check if the plane is full
                # if it isn't
                if len(Plane.passengers) < Plane.model["maxPassenger"]:

                    # add the passenger
                    Plane.addEntity(entity)
                    if self.showFeed:
                        print(
                            f"Passenger, {entity.name} has been added to Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} 💼\n"
                        )

                # otherwise the plane is ready to fly
                else:
                    if self.showFeed:
                        print(
                            f"Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']}, Boarding finished. setting status to Ready ✅\n"
                        )
                    Plane.setStatus("Ready")

    # function for sending the take off signal
    def sendTakeOffSignal(self):

        # check for the planes that are ready
        planesReady = list(filter(lambda x: x.status == "Ready", self.planes))

        # if there are planes
        if planesReady:

            # then select one and tell it to take off
            Plane = random.choice(planesReady)
            Plane.setTakeOff()
            if self.showFeed:
                print(
                    f"Plane {Plane.id} ({Plane.type}): {self.name} --> {Plane.destination['name']} has taken off 🛫\n"
                )

    # function for allowing planes to land
    def sendLandingSignal(self):

        # check if the plane is in flight and inbound for the airport
        planesInFlight = list(filter(lambda x: not x.atAirport, self.planes))

        # there are any
        if planesInFlight:
            # select one and tell it to land
            Plane = random.choice(planesInFlight)
            Plane.setLanding()

            # check if it needs maintenance
            Plane.checkForMaintenance()

            # fuel for the plane has been used
            Plane.resetFuel()

            Plane.setDestination(generateDestination())

            # also unload or unboard any passengers or packages
            Plane.unload()
            if self.showFeed:
                print(
                    f"Plane {Plane.id} ({Plane.type}): {Plane.destination['name']} --> {self.name} has landed! 🛬\n"
                )

    def preformMaintenance(self):

        # get all the planes that have a status of maintenance
        planesOnMaintenance = list(
            filter(lambda x: "Maintenance" in x.status, self.planes)
        )

        # and if there are any planes
        if planesOnMaintenance:

            # choose a random one and preform a check of it
            plane = random.choice(planesOnMaintenance)

            plane.doMaintenance()
            if self.showFeed:
                print(f"Plane {plane.id} ({plane.type}) --> {plane.getStatus()} ⚒️\n")

        # then select one and do then maintenance check on it

    # for sorting planes
    def sortPlanes(self, sortKey):

        sortedPlanes = None

        # sort based on the key that was passed in
        if sortKey == "dest":

            sortedPlanes = sorted(self.planes)

        elif sortKey == "id":

            sortedPlanes = sorted(self.planes, key=lambda x: x.id)

        elif sortKey == "stat":
            sortedPlanes = sorted(self.planes, key=lambda x: x.status)

        #  or dont do sorting if that key wasnt passed in
        else:
            sortedPlanes = self.planes

        return createTable(sortedPlanes)

    def searchForPlane(self, query):

        # change the query to lower case for easier comparison
        query = query.lower()

        # function to help with searching
        def searchFunc(plane):
            # check if the query that the user entered matches any of the following
            if (
                query in plane.id.lower()
                or query in plane.destination["name"].lower()
                or query in plane.status.lower()
            ):
                return True
            else:
                return False

        planesFound = list(filter(searchFunc, self.planes))

        if planesFound:
            return createTable(planesFound)

        else:
            raise AirportException(
                "Search Error", "couldn't find any planes with your query"
            )

    def viewPlane(self, planeId):

        match = None

        # check for if there is a plane that matches the id the user has entered
        for plane in self.planes:
            if plane.id.lower() == planeId.lower():
                match = plane
                break

        if match:
            print(plane)
            if isinstance(plane, PassengerPlane):
                return createTable(plane.passengers, "passengers")
            else:
                return createTable(plane.packages, "cargo")
        else:
            raise AirportException(
                "Search Error", "couldn't find plane, enter a valid ID"
            )

    # prints the state of the airport and the list of current planes
    def __str__(self) -> str:

        planeList = ""

        # find the number of planes that are stationed at the airport
        planesStationed = len(list(filter(lambda x: x.atAirport, self.planes)))

        # get the status of all the planes
        for index, plane in enumerate(self.planes):
            planeList += f"Plane {index+1}\n{plane.__str__()}\n"

        # and display them in the console...
        return (
            f"{self.name} Status\n\n"
            f"Number of Planes Stationed: {planesStationed}\n\n"
            "List of Planes\n\n"
            f"{planeList}\n"
        )
