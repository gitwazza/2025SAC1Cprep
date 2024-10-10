# As of 10 OCt 2024 - this program works, but is missing functionality
# possible student exercise could be to implement the missing parts e.g save list to file,
# delete and edit a record as methods.



# In this example we will look at how we might abstract Bookings
#
# We often use classes because we need to instantiate (or create) multiple instances of a class.
# There are other reasons why OOP is a preferred methodology and a key advantage is that code
# can be more robust by ensuring that only methods within the class are allowed to
# modify and/or directly access an object's attributes.
# We only need one instance of Bookings in this program to represent all bookings.
# So in this instance we are writing this as an OOP program as a demonstration of OOP, but also
# as a demonstration of how OOP can make our code more robust.
#
# There are many ways we could implement this. However, we will take the approach that the
# bookings instance will have the following attributes:
#   books  - is a list of all the booking
# and the following methods:
#   refile() - reads the bookings from a bookings file into a books list
#   safile() - saves the bookings to the bookings file
#   reindbook() - reads an individual booking
#   display_bookings() - displays the list of bookings
#   updatebook() - update an existing booking
#   addbook() - adds a booking to the booking list
#   delbook() - deletes a booking from the booking list
# Keep in mind that management of any database (or in this case a list of bookings) should allow
# for CRUD (create, read, update, delete). The methods above should allow us to implement all of these
# CRUD processes.
# As indicated above, one advantage of OOP programming is that it should
# reduce errors by ensuring that the object's attributes are only manipulated by the methods which
# are defined within the class. So although Python allows object attributes to be modified by
# instructions outside of the class definition - we will avoid doing this to ensure our code is
# implementing robust OOP code. Hence, the only code which directly manipulates the bookings list,
# should exist within the Bookings class definition.
#
# In this example we will store the bookings data in a CSV file. Each line of the CSV file will
# represent a 'record' of an individual booking. The program will read each line into a single record,
# or a single dictionary, within the list.
# Python allows CSV files to be read from and written
# to with relative ease. It is especially simple to read from a CSV file directly into a list of
# dictionaries, and this is what is done in this program.
# This program demonstrates two ways to read a CSV file.

import csv

print("getting started!")


class Bookings:

    def __init__(self):
        self.books = []  # create an empty list which can store the booking list
        self.readfile_ver_b()

    # readfile_ver_a() reads the file of bookings line by line to create a list of dictionaries
    # In most programming languages reading a file, normally requires the programmer
    # to open the file first, then read from the file and then close the file. We can do this
    # in Python.However, it is also possible (as demonstrated below) to use the
    # 'with' statement to access a file. When using a 'with' statement the programmer
    # does not need to write a line of code to close the file, as the file is closed
    # automatically when the 'with' block of code finishes.
    def readfile_ver_a(self):
        with open('allbookings.txt') as file:
            for line in file:
                first, last = line.rstrip().split(",")
                book = {'first': first, 'last': last}
                self.books.append(book)

        # The following line sorts the list based on the 'first' names
        # which were read into the list. Keep in mind that VCE Software Development
        # requires us to know particular sorting algorithms and the code here is
        # not a sorting algorithm.It is simply calling the "sorting" function,
        # which is part of Python, to sort the list of dictionaries. You are not
        # required to understand the inner workings of this sorted() function.
        # You just need to understand that it takes the self.books list as an
        # argument and returns the same list in sorted form.
        self.books = sorted(self.books, key=lambda book: book['first'])

        self.display_bookings()

    # readfile_ver_b() reads the file line by line to create a list of dictionaries
    # This code achieves the same function as readfile_ver_b(). The difference is
    # that in this case we use the csv.DictReader() method.
    def readfile_ver_b(self):
        self.books = []
        with open('allbookings.txt') as file:
            reader = csv.DictReader(file, fieldnames=['first', 'last'])  # creates a DictReader
            for row in reader:
                self.books.append(row)

        # see note in readfile_ver_a(self) above for an explanation of the use of sorted function
        self.books = sorted(self.books, key=lambda book: book['first'])

        self.display_bookings()

    def addbook(self):
        first = input("What is the first name for your booking? ")
        last = input("What is the first name for your booking? ")
        self.books.append({'first': first, 'last': last})
        self.books = sorted(self.books, key=lambda book: book['first'])
        self.display_bookings()



    def display_bookings(self):
        for count in range(len(self.books)):
            print(f'{count} - {self.books[count]}')


def main():
    my_booking = Bookings()
    keep_running = True
    while keep_running:
        print("Choose one of the following functions to perform on your booking")
        print("1 - add a booking")
        print("2 - delete a booking")
        print("3 - edit an existing booking")
        print("9 - exit this program")
        choice = input("type a digit representing one of the above and enter")

        match choice:
            case '1':
                my_booking.addbook()
            case '2':
                pass
            case '3':
                pass
            case '9':
                keep_running = False


if __name__ == "__main__":
    main()
