print("getting started!")


class Booking:

    def __init__(self, num):
        self.num = int(num)
        print(f"booking made for {num} people")


my_booking = Booking(3)
