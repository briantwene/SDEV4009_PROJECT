# Filename: main.py
# Author: Brian Twene
# Date: 9/10/2022

# import util libaries and functions
from random import randint
from threading import Thread, Event
from interface import Interface
import time
from Airplane import CargoPlane, PassengerPlane
from Airport import Airport

from util import (
    generatePassenger,
    generateDestination,
    generateModel,
    generatePlaneId,
    generatePackage,
)

# main function definition


def main(stopEvent):

    # create airport instance
    # and interface instanace
    myAirport = Airport()
    myAirportConsole = Interface()

    # create planes and add them to the airport

    for x in range(2):
        myAirport.addPlane(
            CargoPlane(
                generatePlaneId(), generateDestination(), 0, generateModel(), "Cargo"
            )
        )
        myAirport.addPlane(
            PassengerPlane(
                generatePlaneId(),
                generateDestination(),
                0,
                generateModel(),
                "Passenger",
            )
        )

    print("Initiating Airport Duties....\n")

    # add the airport instance and stop flag event in the console for later use
    myAirportConsole.setAirport(myAirport)
    myAirportConsole.setEventFunc(stopEvent)

    # start the airport duties on a separate thread
    Thread(target=runDuties, args=(myAirport, stopEvent)).start()

    # start the console for the user to interact with
    myAirportConsole.cmdloop("Input commands here\n")


# function for running airport duties
def runDuties(myAirport, stopEvent):

    while 1:

        action = randint(1, 6)

        if action == 1:
            myAirport.fuelPlane()
        elif action == 2:
            myAirport.onLoad(generatePassenger())
        elif action == 3:
            myAirport.onLoad(generatePackage())
        elif action == 4:
            myAirport.sendTakeOffSignal()
        elif action == 5:
            myAirport.sendLandingSignal()
        elif action == 6:
            myAirport.preformMaintenance()

        # if the stop flag is set exit out of the loop
        if stopEvent.is_set():
            print("Halting Duties and exiting - Good Bye 👋\n")
            break

        time.sleep(0.5)
        # start = time.time()


try:
    stopEvent = Event()
    main(stopEvent)
# if the user use Ctrl+C to force fully exit
except KeyboardInterrupt:
    # catch the exception
    print("Force closing app gracefully!")
    # tell the thread to stop
    stopEvent.set()
