# Filename: main.py
# Author: Brian Twene
# Date: 9/10/2022

# import util libaries and functions
from random import randint
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
def main():

    # create airport instance
    myAirport = Airport()

    # create planes and add them to the airport

    myAirport.addPlane(
        CargoPlane(generatePlaneId(), generateDestination(), 0, generateModel())
    )
    myAirport.addPlane(
        PassengerPlane(generatePlaneId(), generateDestination(), 0, generateModel())
    )

    # print the airport status
    print(myAirport)

    print("Initiating Airport Duties....\n")
    time.sleep(5)
    start = time.time()

    # randomly do airport duties
    while 1:
        action = randint(1, 5)

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

        time.sleep(1)

        # when ten or more seconds have passed display the status of the airport
        if time.time() - start >= 10:
            print(myAirport)
            start = time.time()


# call main function
main()
