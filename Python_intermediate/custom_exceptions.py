class MyCustomException(Exception):
    pass


# raise MyCustomException


class IncorrectValueError(Exception):

    def __init__(self, value):
        message = f"Got a bad value:  {value}"
        super().__init__(message)
        self.value = value


my_value = 998

if my_value > 998:
    raise IncorrectValueError(my_value)
else:
    print("Great all is fine!")
