# Filename: util.py
# Author: Brian Twene
# Date: 04/10/2022

# import needed classes and libraries
import random
import string
from arrayNames import names
from cargo import Passenger, Cargo

# list of avaliable destinations and their fuel costs
destinationMap = [
    {"name": "New York", "cost": 10},
    {"name": "Amsterdam", "cost": 2},
    {"name": "Paris", "cost": 2},
    {"name": "Berlin", "cost": 3},
    {"name": "Dubai", "cost": 7},
    {"name": "Rio de Janeiro", "cost": 10},
    {"name": "Cairo", "cost": 8},
    {"name": "Rome", "cost": 4},
    {"name": "Warsaw", "cost": 4},
    {"name": "New York", "cost": 10},
    {"name": "Lisbon", "cost": 2},
    {"name": "Madrid", "cost": 2},
    {"name": "Montreal", "cost": 10},
    {"name": "London", "cost": 1},
    {"name": "Belfast", "cost": 1},
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
]

# list of plane models to choose from
planeModels = [
    {"model": "Boeing 747-8", "maxPassenger": 5, "maxCargoWeight": 5},
    {"model": "Airbus A380", "maxPassenger": 5, "maxCargoWeight": 5},
]

# list of passenger classes to choose from
classes = ["Business", "Economy"]

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
