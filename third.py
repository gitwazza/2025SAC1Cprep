# This is an extension - as the content is not required for an understanding of OOP within the VCE.
# However, this program introduces Class methods and class variables/attributes which can be
# used when creating OOP programs in Python.
# In the last two program we introduced a class Bookings - to represent all the bookings and hold
# those bookings in a list. And we also introduced a Booking class to represent individual Bookings.
# As the main aim of the Bookings class in the second program was to hold a list, another alternative is
# to do away with the Bookings class and just replace it with a list. In Python there's an appropriate
# way to do this with what's known as a 'class variable'. The following code demonstrates this by
# removing the 'Bookings' class and instead using a list called 'bookings' inside the Booking class.
# There is only a single instance of the bookings variables created, regardless of how many 'Booking'
# instances are instantiated.
# An alternative way of achieving a similar outcome might be to create the bookings list as a global
# variable rather than as a class variable within the Booking class.
# The program also introduces a class method (@classmethod). Class methods operate on the class rather
# than like methods that operate on an instance of the class. By using class variables and class
# methods we encapsulate most of the functionality in a single class definition.
# another

import csv

print("getting started!")

class Booking:
    bookings = []
    def __init__(self, first, last):
        # as property function exists for 'first' the following will call the setter
        # function for first
        self.first = first
        self.last = last
        print(f'just added {first} {last}')

    def __str__(self):
        return f'{self.first} {self.last}'

    def __del__(self):
        print('destroying the object')

    # This is getter function
    @property
    def first(self):
        return self._first

    # This is a corresponding setter function for @property
    @first.setter
    def first(self, first):
        if not first:
            raise ValueError("first name empty")
        self._first = first

    @classmethod
    def add_booking(cls):
        first = input('What is your first name: ')
        last = input('What is your last name: ')

        try:
            # The following code looks booking = Booking(first, last)
            booking = cls(first, last)
        except ValueError as error:
            # del booking
            print(error)
            print("entry not added")
        else:
            # cls.bookings.append(booking)
            print(f'booking is {booking}')

        # print(f"Type of class {type(booking)}")
        # # newbook = Booking(first, last)
        # # self.books.append(newbook)
        # print(f'have created a booking {booking}')
        # print(f'length of bookings {len(cls.bookings)}')
        # cls.bookings.append(booking)
        # print(f'length of bookings {len(cls.bookings)} after')
        # print('next print bookings')
        # print(cls.bookings)

    @classmethod
    def show_bookings(cls):
        print(f'length of bookings {len(cls.bookings)} in show bookings')
        print(cls.bookings)
        print(cls.bookings[0])
        for booking in cls.bookings:
            print('into loop')
            print(booking.first)


# class Bookings:
#
#     def __init__(self, num):
#         self.booklist = []
#         self.num = int(num)
#         print(f"booking made for {num} people")
#
#     # reads each line into a list and then sorts and prints
#
#     # reads the file line by line to create a list of dictionaries
#     def refile3(self):
#         books = []
#         with open('allbookings.txt') as file:
#             for line in file:
#                 first, last = line.rstrip().split(",")
#                 # book = {}             # these 3 lines more verbose than subsequent line
#                 # book['first'] = first
#                 # book['last'] = last
#                 book = {'first': first, 'last': last}
#                 books.append(book)
#
#         for book in sorted(books, key=lambda book: book['first']): #lambda function
#             print(book)
#
#     def refile4(self):
#         self.books = []
#         with open('allbookings.txt') as file:
#             reader = csv.reader(file) # creates a DictReader
#             for row in reader:
#                 newbook = Booking(row[0], row[1])
#                 self.books.append(newbook)
#
#         for book in self.books:
#             print(book)
#         #         books.append({'first': row['first'], 'last': row['last']})
#         #
#         # for book in sorted(books, key=lambda book: book['first']): #lambda function
#         #     print(book)
#
#     def entervalue(self):
#
#         while True:
#             first = input('What is your first name: ')
#             last = input('What is your last name: ')
#
#             try:
#                 newbook = Booking(first, last)
#
#             except ValueError as error:
#                 print(error)
#                 print("entry not added")
#
#             else:
#                 # only add the new book to the list if no error occurred
#                 self.books.append(newbook)
#
#             ask = input("do you want to add more (y/n)")
#             if ask == "n":
#                 break
#
#
#         for book in self.books:
#             print(book)


def main():
    add_a_booking = True
    while add_a_booking == True:
        Booking.add_booking()
        answ = input("Do you want to add another booking? (y/n): ")
        if answ != 'y':
            add_a_booking = False

    print('about to show bookings')
    Booking.show_bookings()
    # my_booking = Bookings(3)
    # my_booking.refile4()
    # my_booking.entervalue()

if __name__ == "__main__":
    main()
