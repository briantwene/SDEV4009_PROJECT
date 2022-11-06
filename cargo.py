# Filename: cargo.py
# Author: Brian Twene
# Date: 9/10/2022

# Passenger class definition
class Passenger:

    # constructor for the class
    def __init__(self, name, planeClass, seatPosition, passengerAge) -> None:
        # passing data to instance variables
        self.name = name
        self.seatClass = planeClass
        self.seatNumber = seatPosition
        self.age = passengerAge

    # getters
    def getName(self):
        return self.name

    def getSeatClass(self):
        return self.seatClass

    def getSeatNumber(self):
        return self.seatNumber

    def getAge(self):
        return self.age

    # setters
    def setName(self, name):
        self.name = name

    def setSeatClass(self, seatClass):
        self.seatClass = seatClass

    def setSeatNumber(self, seatNumber):
        self.seatNumber = seatNumber

    def setAge(self, age):
        self.age = age

    # string representation of the passenger
    def __str__(self) -> str:
        return (
            f"\tName: {self.name}\n"
            f"\tClass: {self.seatClass}\n"
            f"\tSeat No: {self.seatNumber}\n"
            f"\tAge: {self.age}\n\n"
        )


# cargo class definition
class Cargo:

    # constructor for the class
    def __init__(self, id, name, weight, courier) -> None:
        # passing data from the init into the instance variables
        self.id = id
        self.name = name
        self.weight = weight
        self.courier = courier

    # getter methods

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getCourier(self):
        return self.courier

    # setter methods

    def setId(self, newId):
        self.id = newId

    def setName(self, name):
        self.name = name

    def setWeight(self, newWeight):
        self.weight = newWeight

    def setCourier(self, courier):
        self.courier = courier

    # string representation

    def __str__(self) -> str:
        return (
            f"\tPackage ID: {self.id}\n"
            f"\tName: {self.name}\n"
            f"\tWeight: {self.weight}\n"
            f"\tCourier: {self.courier}\n\n"
        )
