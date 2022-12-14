# Filename: util.py
# Author: Brian Twene
# Date: 04/10/2022

# import needed classes and libraries
from tabulate import tabulate
import random
import string
from arrayNames import names
from cargo import Passenger, Cargo


# list of avaliable destinations and their fuel costs
destinationMap = [
    {"name": "New York (JFK)", "cost": 10},
    {"name": "New York (LGA)", "cost": 10},
    {"name": "New York (EWR)", "cost": 10},
    {"name": "Amsterdam (AMS)", "cost": 2},
    {"name": "Paris (CDG)", "cost": 2},
    {"name": "Paris (ORY)", "cost": 2},
    {"name": "Paris (BVA)", "cost": 2},
    {"name": "Berlin (BER)", "cost": 3},
    {"name": "Frankfurt (FRA)", "cost": 3},
    {"name": "Munich (MUC)", "cost": 3},
    {"name": "Dubai (DXB)", "cost": 7},
    {"name": "Rio de Janeiro (GIG)", "cost": 10},
    {"name": "Cairo (CAI)", "cost": 8},
    {"name": "Rome (FCO)", "cost": 4},
    {"name": "Warsaw (WAW)", "cost": 4},
    {"name": "Orlando (MCO)", "cost": 10},
    {"name": "Lisbon (LIS)", "cost": 2},
    {"name": "Madrid (MAD)", "cost": 2},
    {"name": "Barcelona (BCN)", "cost": 2},
    {"name": "Montreal (YUL)", "cost": 10},
    {"name": "London (LGW)", "cost": 1},
    {"name": "London (STN)", "cost": 1},
    {"name": "London (LTN)", "cost": 1},
    {"name": "Edinburgh (EDI)", "cost": 1},
    {"name": "Glasgow (GLA)", "cost": 1},
    {"name": "Aberdeen (ABZ)", "cost": 1},
    {"name": "Belfast", "cost": 1},
    {"name": "Perth (PER)", "cost": 15},
    {"name": "Accra (ACC)", "cost": 8},
    {"name": "Lagos (LOS)", "cost": 8},
    {"name": "Tunis (TUN)", "cost": 4},
    {"name": "Johannesburg (JNB)", "cost": 11},
]

# list of packages to generate from
packageList = [
    "Scooter",
    "Bike",
    "Computer",
    "Gaming-Chair",
    "Desk",
    "Drawers",
    "Mattress",
    "Bed",
    "RollerBlades",
    "Toolkit",
    "Gaming Console",
    "T-shirt",
    "SSD",
    "HDD",
    "Phone",
]

# list of plane models to choose from
planeModels = [
    {"model": "Boeing 747-8", "maxPassenger": 200, "maxCargoWeight": 10},
    {"model": "Airbus A380", "maxPassenger": 150, "maxCargoWeight": 10},
    {"model": "Boeing 777-8X", "maxPassenger": 315, "maxCargoWeight": 10},
]

# list of passenger classes to choose from
classes = ["Business", "Premium", "Economy"]

# list of couriers to choose from
couriers = ["DHL", "UPS", "FedEx", "TNT", "Amazon Prime"]


# function for generating passenger classes
def generatePassenger():

    # get the name age and class for the passenger
    name = f"{random.choice(names)} {random.choice(names)}"
    age = random.randint(1, 90)
    passengerClass = random.choice(classes)

    # return a passenger object with this data
    return Passenger(name, passengerClass, None, age)


# return a random destination for the plane
def generateDestination():

    return random.choice(destinationMap)


# return a random plane model
def generateModel():
    return random.choice(planeModels)


# generate a plane
def generatePlaneId(length=8):

    randId = ""

    # add a character based on the length passed into the function
    for x in range(length):
        randId += random.choice(string.ascii_uppercase + string.digits)

    return randId


# function for generating package class
def generatePackage():
    # generate data from other functions and data structures
    packageId = generatePlaneId(5)
    name = f"{generatePlaneId(3)}-{random.choice(packageList)}"
    weight = random.randint(1, 5)
    courier = random.choice(couriers)

    # then return a package object with this data
    return Cargo(packageId, name, weight, courier)


# function for creating the table
def createTable(data, type="planes"):

    col_names = []
    tableData = []

    # generate table data based on the type
    match (type):

        # if an array of planes
        case "planes":
            col_names = ["ID", "Destination", "Status", "Model", "Type"]
            for plane in data:

                tableData.append(
                    [
                        plane.id,
                        plane.destination["name"],
                        plane.status,
                        plane.model["model"],
                        plane.type,
                    ]
                )
        # if an array of passengers
        case "passengers":
            col_names = ["Name", "Class", "Age"]
            for passenger in data:

                tableData.append(
                    [
                        passenger.name,
                        passenger.seatClass,
                        passenger.age,
                    ]
                )
        # if an array of cargo
        case "cargo":
            col_names = ["Package ID", "Name", "Weight (Kg)", "Courier"]
            for cargo in data:

                tableData.append(
                    [
                        cargo.id,
                        cargo.name,
                        cargo.weight,
                        cargo.courier,
                    ]
                )

    # first loop through the array

    # the for each item in the array will make an array that would have all of the information

    # return table object with the data
    return tabulate(tableData, headers=col_names)
