import datetime


class Booking:
    def __init__(self, name, date, t_from, t_to, seats):
        self.name = name
        self.date = date
        self.t_from = t_from
        self.t_to = t_to
        self.seats = seats

    def __str__(self):
        return self.name + ': ' + str(self.date) + ' (' + \
            str(self.t_from)+ ' - ' + str(self.t_to) + ') ' + str(self.seats)


class Restaurant:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bookings = []

    def print_bookings(self):
        for booking in self.bookings:
            print(booking)

    def print_bookings_of_date(self, date):
        for booking in self.bookings:
            if date == booking.date:
                print(booking)

    def occupancy(self, date, t_from, t_to):
        total = 0
        for booking in self.bookings:
            if date == booking.date:
                if booking.t_from <= t_from < booking.t_to:
                    total += booking.seats
                elif booking.t_from <= t_to < booking.t_to:
                    total += booking.seats
                elif t_from < booking.t_from and t_to > booking.t_to:
                    total += booking.seats
        return total

    def make_reservation(self, name, persons, date, t_from, t_to):
        occ = self.occupancy(date, t_from, t_to)
        availability = self.capacity - occ
        if availability >= persons:
            self.bookings.append(Booking(name, date, t_from, t_to, persons))
            return True
        else:
            return False


if __name__ == '__main__':
    restaurant = Restaurant(36)
    restaurant.bookings.append(Booking('John', datetime.date(2023, 4, 28),
                                       datetime.time(13, 00), datetime.time(14, 30), 5))
    restaurant.bookings.append(Booking('Peter', datetime.date(2023, 4, 28),
                                       datetime.time(12, 30), datetime.time(13, 30), 7))
    restaurant.bookings.append(Booking('Mary', datetime.date(2023, 4, 28),
                                       datetime.time(14, 00), datetime.time(15, 30), 2))
    restaurant.bookings.append(Booking('Mary', datetime.date(2023, 4, 29),
                                       datetime.time(14, 00), datetime.time(15, 30), 5))
    # restaurant.print_bookings()
    # print(restaurant.occupancy(datetime.date(2023, 4, 28), datetime.time(12, 00), datetime.time(16, 00)))
    # print(restaurant.occupancy(datetime.date(2023, 4, 28), datetime.time(12, 00), datetime.time(12, 30)))
    # print(restaurant.occupancy(datetime.date(2023, 4, 28), datetime.time(15, 00), datetime.time(16, 30)))

    while True:
        print("1. Make reservation")
        print("2. Print reservations for date")
        print("0. EXIT")
        choice = int(input("Choose: "))

        try:
            if choice == 1:
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                hfrom = int(input("Hour from: "))
                mfrom = int(input("Minutes from: "))
                hto = int(input("Hour to: "))
                mto = int(input("Minutes to: "))
                persons = int(input("Persons: "))
                name = input("Name: ")
                if restaurant.make_reservation(name, persons, datetime.date(year, month, day),
                                               datetime.time(hfrom, mfrom), datetime.time(hto, mto)):
                    print("Reservation set")
                else:
                    print("No availability")
            elif choice == 2:
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                restaurant.print_bookings_of_date(datetime.date(year, month, day))
            elif choice == 0:
                print("Bye!")
                break
        except ValueError:
            print("You gave wrong values")


