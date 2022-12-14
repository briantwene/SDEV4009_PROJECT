# user defined exception
class AirportException(Exception):
    # constructor
    def __init__(self, expression, message) -> None:
        self.expression = expression
        self.message = message

    # string representation
    def __str__(self) -> str:
        return f"{self.expression} - {self.message}"
