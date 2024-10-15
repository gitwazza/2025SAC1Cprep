# to do - can introduce private and protected attributes as well as getter and setter
# and have students learn how they could use either an attribute or private property or
# protected property/attribute

# In this program we can extend the OOP nature of first.py by creating another class
# In the same way the Bookings class abstracts the Booking list as an object, we can
# create a Booking class to abstract individual bookings within the Bookings list.

# When creating a 'Booking' class we ideally want the class attributes to be
# accessed directly by functions (methods) within the class.
#
# As adding or updating a booking should ideally involve some form of validation we
# need to consider where validation code should occur. For example, when adding a booking
# should our code's __inti__ method create an empty booking, which our code subsequently
# adds attribute values to, or should we add all the attribute values when the __init__
# method is run. Either way there is an issue, in that as soon as the Booking object is
# instantiated it has been created, and so effectively we may have an Booking object
# with some incorrect value. There are several ways we might try to solve this dilemma
# one is that we might try to validate data prior to attempting to create the new booking
# or the other way is to leave the validation up to methods within the Booking class.
# The second method is more inline with OOP as we are making the code within the class
# responsible for it's own functionality. However, we need to handle the fact that
# we may attempt to make an object and not succeed but still have an object with an
# error that we don't want.
# This introduces some further functionality used in Python OOP.
# This is getter and setter functions.

import csv

print("getting started!")

# In this example a 'property function' is introduced, and this involves the introduction
# of getter and setter functions.
# The syntax for getter and setter functionality in Python is a bit unusual.
#  As an example the 'first'
# name will actually be stored in the attribute 'self._first'. Whereas 'self.first',
# which does not include the '_' infront of 'first' represent the property function.
class Booking:
    def __init__(self, first, last):
        # as property function exists for 'first' the following will call the setter
        # function for first
        self.first = first
        self.last = last
        print(f'just added {first} {last}')

    def __str__(self):
        return f'{self.first} {self.last}'

    def __del__(self):
        # This can be used during debugging to show that the object was destroyed
        print('destroying the object')

    # This is getter function
    @property
    def first(self):
        return self.__first

    # This is a corresponding setter function for @property
    @first.setter
    def first(self, first):
        if not first:
            raise ValueError("first name empty")
        self.__first = first

    # This is getter function
    @property
    def last(self):
        return self.__first

    # This is a corresponding setter function for @property
    @last.setter
    def last(self, last):
        print("running last...............")
        if not last:
            raise ValueError("last name empty")
        self.__last = last


class Bookings:

    def __init__(self, num):
        self.booklist = []
        self.num = int(num)
        print(f"booking made for {num} people")

    # reads each line into a list and then sorts and prints

    # reads the file line by line to create a list of dictionaries

    def refile4(self):
        self.books = []
        with open('allbookings.txt') as file:
            reader = csv.reader(file) # creates a DictReader
            for row in reader:
                newbook = Booking(row[0], row[1])
                self.books.append(newbook)

        for book in self.books:
            print(book)
        #         books.append({'first': row['first'], 'last': row['last']})
        #
        # for book in sorted(books, key=lambda book: book['first']): #lambda function
        #     print(book)

    def entervalue(self):

        while True:
            first = input('What is your first name: ')
            last = input('What is your last name: ')

            try:
                newbook = Booking(first, last)

            except ValueError as error:
                print(error)
                print("entry not added")

            else:
                # only add the new book to the list if no error occurred
                self.books.append(newbook)

            ask = input("do you want to add more (y/n)")
            if ask == "n":
                break


        for book in self.books:
            print(book)


def main():
    my_booking = Bookings(3)
    my_booking.refile4()
    my_booking.entervalue()

if __name__ == "__main__":
    main()
