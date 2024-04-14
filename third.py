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
        print('called the add_booking class method')
        booking = cls('warren', 'sutton')
        print(f"Type of class {type(booking)}")
        # newbook = Booking(first, last)
        # self.books.append(newbook)
        print(f'have created a booking {booking}')
        print(f'length of bookings {len(cls.bookings)}')
        cls.bookings.append(booking)
        print(f'length of bookings {len(cls.bookings)} after')
        print('next print bookings')
        print(cls.bookings)

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
    Booking.add_booking()
    print('about to show bookings')
    Booking.show_bookings()
    # my_booking = Bookings(3)
    # my_booking.refile4()
    # my_booking.entervalue()

if __name__ == "__main__":
    main()
