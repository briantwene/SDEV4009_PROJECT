from cmd import Cmd
import keyboard
from AirportException import AirportException


# interface class declaration extends the CMD object


class Interface(Cmd):

    prompt = "> "
    intro = "Input your command here \n"

    # constrctor

    myAirport = None
    eventFunc = None
    sortOptions = ["id", "dest", "stat", "none"]

    # each of the functions that start with do_* are commands that the user can enter

    # for the "feed" command
    def do_feed(self, args):
        print("Press Q key to quit feed\n\n")
        self.myAirport.setShowFeed(True)

        while not keyboard.is_pressed("q"):
            pass

        self.myAirport.setShowFeed(False)

        print("Live Feed has stopped showing - duties running in background\n\n")

    # for the "list" command
    def do_list(self, sortKey):

        try:
            # get the argument out by splitting
            parsedArgs = sortKey.split()
            sortKey = "none"

            # check if there are were any arguments passed in
            if len(parsedArgs) > 1:
                raise AirportException(
                    "Input Error", "cant have more than one argument\n"
                )
            # if the user entered in the correct amount
            elif len(parsedArgs) != 0:
                # get that argument
                sortKey = parsedArgs[0]

            # check if that argument is one of the sorting options
            if sortKey not in self.sortOptions:
                raise AirportException(
                    "Input Error", "Please enter a valid sorting option\n"
                )
            # if it is then get the list of planes
            else:
                print(self.myAirport.sortPlanes(sortKey) + "\n")

            # print(self.myAirport.searchForPlane(query))
        except AirportException as error:
            print(error)

        # print(f"sorting key: {sortKey}")

    # for the "search command"
    def do_search(self, args):

        try:
            # get the argument out by splitting
            parsedArgs = args.split()
            query = None

            # check if there are were any arguments passed in
            if len(parsedArgs) > 1:
                raise AirportException(
                    "Input Error", "cant have more than one argument\n"
                )
            # if the user entered in the correct amount
            elif len(parsedArgs) != 0:
                # get that argument
                query = parsedArgs[0]
            else:
                raise AirportException(
                    "Input Error",
                    "Please enter a query (Flight ID, Destination, Status)\n",
                )

            # if all is good then run the search query

            print(self.myAirport.searchForPlane(query) + "\n")
        except AirportException as error:
            # Printing the result of the searchForPlane function.
            print(error)

    # for the "view" command
    def do_view(self, args):

        try:
            # get the argument out by splitting
            parsedArgs = args.split()
            planeId = None

            # check if the user entered more than 1 argument
            if len(parsedArgs) > 1:
                raise AirportException(
                    "Input Error", "cant have more than one argument\n"
                )
            # if the user entered in the correct amount (1)
            elif len(parsedArgs) != 0:
                # then get that argument
                planeId = parsedArgs[0]

            # otherwise raise execption
            else:
                raise AirportException(
                    "Input Error",
                    "Please enter the Flight ID\n",
                )
                # if it is then get the list of planes

            # if all good then find and display the planes stats
            print(self.myAirport.viewPlane(planeId) + "\n")

        except AirportException as error:
            print(error)

    # setter function for adding the airport to the class
    def setAirport(self, airport):
        self.myAirport = airport

    # function for adding the event flag to the class
    def setEventFunc(self, stopEvent):
        self.setEventFunc = stopEvent

    # function for the "exit command"
    def do_exit(self, args):
        # set the flag to true so that the tread running airport duties is closed
        self.setEventFunc.set()
        # raise system exit exception to exit the console
        raise SystemExit()
