'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
        
class Play:

    def __init__(self, id, name, numSeats, date, status = True):
        self.__id = id
        self.__name = name
        self.__numSeats = numSeats
        self.__date = date
        self.__status = status

    #Accessor Methods
    def get_Name(self):
        return self.__name
    def get_Seats(self):
        return self.__numSeats
    def get_Status(self):
        return self.__status

    #Mutator Methods
    def seats_left(self, numSeats):
        self.__numSeats = numSeats - 1

    def set_status(self, status):
        self.__status = False


class Booking:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

