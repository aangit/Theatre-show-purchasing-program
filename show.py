from seat import Seat
from days_enum import DaysEnum
from typing import List
from seat_type_enum import SeatType


class Show:
    name: str
    day: DaysEnum
    time: str
    seats: List[Seat]
    code: str

    def __init__(self, name: str, day: DaysEnum, time: str, code: str, vip_price: float, parter_price: float):
        self.name = name
        self.day = day
        self.time = time
        self.code = code
        self.seats = []
        self.__add_seats(vip_price, parter_price)

    def __str__(self) -> str:
        result = f"Show: {self.name}, is played on: {self.day.name}, at: {self.time}, with code: {self.code}"
        return result

    def __repr__(self) -> str:
        result = f"Show: {self.name}, is played on: {self.day.name}, at: {self.time}, with code: {self.code}"
        return result

    def __add_seats(self, vip_price: float, parter_price: float) -> None:
        """
        It creates a list of seats and adds them to the seats list of the object.
        
        :param vip_price: float
        :type vip_price: float
        :param parter_price: float
        :type parter_price: float
        """
        for i in range(1, 5):
            for j in range(1, 16):
                new_seat = Seat(j, i, SeatType.VIP, vip_price)
                self.seats.append(new_seat)
        for i in range(5, 16):
            for j in range(1, 16):
                new_seat = Seat(j, i, SeatType.PARTER, parter_price)
                self.seats.append(new_seat)

    def check_available_seats(self, number_of_seats: int, seat_type: SeatType):
        """
        "Check if the number of seats requested is less than or equal to the number of available seats."
        
        This is a very simple function, but it's a good example of how to write a docstring
        
        :param number_of_seats: int
        :type number_of_seats: int
        :param seat_type: SeatType
        :type seat_type: SeatType
        :return: The number of seats requested is being compared to the number of available seats.
        """
        return number_of_seats <= self.number_of_available_seats(seat_type)

    def number_of_available_seats(self, seat_type: SeatType):
        """
        It returns the number of seats that are not reserved and are of the requested seat type.
        
        :param seat_type: SeatType
        :type seat_type: SeatType
        :return: A list of seats that are not reserved and are of the seat type specified.
        """
        return len([seat for seat in self.seats if seat.is_reserved == False and seat.seat_type == seat_type])

    def get_number_of_all_available_seats(self):
        """
        It returns the number of seats that are not reserved.
        :return: The number of seats that are not reserved.
        """
        return len([seat for seat in self.seats if seat.is_reserved == False])

    def change_show_time(self, new_time: str) -> None:
        """
        This function changes the time of a show.
        
        :param new_time: The new time of the show
        :type new_time: str
        """
        self.time = new_time

    def get_ticket_price(self):
        """
        It returns a dictionary with the seat type as the key and the price as the value.
        :return: A dictionary with the key being the seat type and the value being the price.
        """
        prices = {}
        for seat in self.seats:
            if seat.seat_type == SeatType.VIP:
                price1 = seat.price
                prices[SeatType.VIP.name] = price1
            elif seat.seat_type == SeatType.PARTER:
                price2 = seat.price
                prices[SeatType.PARTER.name] = price2
        return prices

    def get_revenue(self):
        """
        It returns the sum of the prices of all the seats that are reserved. This method is lated used in class Theatre
        in methods get_best_selling_show and least_selling show.
        :return: The sum of the prices of all the seats that are reserved.
        """
        return sum([seat.price for seat in self.seats if seat.is_reserved])
