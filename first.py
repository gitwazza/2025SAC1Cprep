import csv

print("getting started!")


class Booking:

    def __init__(self, num):
        self.num = int(num)
        print(f"booking made for {num} people")

    # reads each line into a list and then sorts and prints
    def refile(self):
        books = []
        with open('allbookings.txt') as file: #default is 'r'
            for line in file:
                books.append(line.rstrip())
        for book in sorted(books):
            print(book)

    # reads and prints file without storing in list, but reads directly into
    # two variables 'first' and 'last'
    def refile2(self):
        with open('allbookings.txt') as file:
            for line in file:
                first, last = line.rstrip().split(",") # reads into 2 variables
                print(f'Hi {first} {last}')

    # reads the file line by line to create a list of dictionaries
    def refile3(self):
        books = []
        with open('allbookings.txt') as file:
            for line in file:
                first, last = line.rstrip().split(",")
                # book = {}             # these 3 lines more verbose than subsequent line
                # book['first'] = first
                # book['last'] = last
                book = {'first': first, 'last': last}
                books.append(book)

        for book in sorted(books, key=lambda book: book['first']): #lambda function
            print(book)

    def refile4(self):
        books = []
        with open('allbookings.txt') as file:
            reader = csv.DictReader(file) # creates a DictReader
            for row in reader:
                books.append({'first': row['first'], 'last': row['last']})

        for book in sorted(books, key=lambda book: book['first']): #lambda function
            print(book)


my_booking = Booking(3)
my_booking.refile4()
