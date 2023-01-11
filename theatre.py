from typing import List, Tuple
from show import Show
from seat_type_enum import SeatType
from days_enum import DaysEnum
from seat import Seat


class Theatre:
    name: str
    shows: List[Show]

    def __init__(self, name: str, shows: List[Show] = []) -> None:
        """
        This function takes in a name and a list of shows and assigns the name to the name attribute and
        the shows to the shows attribute
        
        :param name: str
        :type name: str
        :param shows: List[Show] = []
        :type shows: List[Show]
        """
        self.name = name
        self.shows = shows

    def __str__(self) -> str:
        result = f"Theatre name is {self.name}, and has the following shows: {self.shows}"
        return result

    def __repr__(self) -> str:
        result = f"Theatre name is {self.name}, and has the following shows: {self.shows}"
        return result

    def add_show(self, show: Show):
        """
        It adds a show to the list of shows if the show is not already in the list
        
        :param show: Show
        :type show: Show
        """
        if show not in self.shows:
            self.shows.append(show)

    def remove_show(self, show: Show):
        """
        It removes a show from the list of shows
        
        :param show: Show
        :type show: Show
        """
        self.shows.remove(show)

    def get_show_timetable(self, name: str) -> List[Show]:
        return [show for show in self.shows if show.name == name]

    def get_show_by_code(self, show_code: str) -> Show:
        """
        It loops through all the shows in the list of shows, and if it finds a show with the same code
        as the one passed in, it returns that show. Otherwise, it returns None
        
        :param show_code: The code of the show you want to get
        :type show_code: str
        :return: The show object
        """
        for show in self.shows:
            if show.code == show_code:
                return show
        return None

    def get_show_by_name(self, show_name: str):
        """
        It loops through the shows in the list of shows and returns the show that has the same name as
        the show_name parameter
        
        :param show_name: The name of the show you want to get
        :type show_name: str
        :return: The show object
        """
        for show in self.shows:
            if show.name == show_name:
                return show

    def buy_tickets(self, show_code: str, number_of_tickets: int, name: str, seat_type: SeatType) -> Tuple[str, List[Seat]]:
        """
        It checks if there are enough seats of the requested type, if not, it checks if there are enough
        seats of any type, if not, it checks if there are enough seats of the requested type in any
        other show on the same day, if not, it checks if there are enough seats of the requested type in
        any other show, if not, it returns an error message.

        
        
        :param show_code: str
        :type show_code: str
        :param number_of_tickets: int, name: str, seat_type: SeatType
        :type number_of_tickets: int
        :param name: str
        :type name: str
        :param seat_type: SeatType
        :type seat_type: SeatType
        :return: A tuple of two values. The first value is a string and the second value is a list of
        seats.
        """
        show = self.get_show_by_code(show_code)
        booked_seats = []
        if show.check_available_seats(number_of_tickets, seat_type):
            for seat in show.seats:
                if seat.seat_type == seat_type and not seat.is_reserved:
                    seat.book_seat(name)
                    booked_seats.append(seat)
                    number_of_tickets -= 1
                    if number_of_tickets == 0:
                        Theatre.save_bought_tickets(booked_seats, show)
                        return None, booked_seats

        else:
            other_seat_types = []

            for seat_enu in SeatType:
                if seat_enu != seat_type and show.check_available_seats(number_of_tickets, seat_enu):
                    other_seat_types.append(seat_enu)
            if other_seat_types:
                return f"There are not available seats in this seat type. Available ones are in {','.join([str(seat.name) for seat in other_seat_types])}", None

            shows_on_same_day = [
                s for s in self.shows if s.day == show.day and s.code != show.code and s.check_available_seats(number_of_tickets, seat_type)]
            if shows_on_same_day:
                return(
                    f"There are not enough tickets for this show. See the next available shows on {shows_on_same_day}", None)

            alternatives = [s for s in self.shows if s.check_available_seats(
                number_of_tickets, seat_type) and s.code != show.code]
            if alternatives:
                return(
                    f"There are not enough tickets for this show. See the next available shows: {alternatives}", None)

            return ("Sorry, no available shows.", None)

    @staticmethod
    def save_bought_tickets(booked_seats: List[Seat], show: Show) -> None:
        """
        It takes a list of seats and a show, and then writes to a file the name of the guest, the row
        and seat number of the seat, and the name of the show
        
        :param booked_seats: List[Seat] - a list of Seat objects
        :type booked_seats: List[Seat]
        :param show: Show
        :type show: Show
        """
        with open(f"tickets/{show.name}_{show.day.name}.txt", "a") as bookings:
            # napraviti folder tickets
            for seat in booked_seats:
                bookings.write(
                    f"{seat.guest_name} has booked a ticket in the row {seat.row} and seat number is {seat.seat_number} for the show {show.name}\n")

    def get_show_availability(self, seat_type: SeatType) -> dict:
        """
        It returns a dictionary of show codes and the number of available seats for each show
        
        :param seat_type: SeatType
        :type seat_type: SeatType
        :return: A dictionary of show codes and the number of available seats for that show.
        """
        availability = {}
        for show in self.shows:
            availability[show.code] = show.number_of_available_seats(seat_type)
        return availability

    def get_percentage_of_availability(self, seat_type: SeatType) -> dict:
        """
        It returns a dictionary of the percentage of available seats for each show, for a given seat
        type
        
        :param seat_type: SeatType
        :type seat_type: SeatType
        :return: A dictionary with the percentage of available seats for each show.
        """
        perc_availability = {}
        for show in self.shows:
            num_seats = len(show.seats)
            num_available_seats = show.number_of_available_seats(seat_type)
            perc_availability[show.code] = round(
                (num_available_seats / num_seats) * 100, 2)
        return perc_availability

    def get_total_availability(self)-> dict:
        """
        It returns a dictionary of all the shows in the theater, with the show code as the key and the
        number of available seats as the value
        :return: A dictionary of all the shows and the number of available seats.
        """
        all_shows = {}
        for show in self.shows:
            all_shows[show.code] = show.get_number_of_all_available_seats()
        return all_shows

    def get_all_shows(self) -> List[Show]:
        """
        It returns a list of all the shows in the database
        :return: A list of all the shows in the shows list.
        """
        all_shows = []
        for show in self.shows:
            all_shows.append(show)
        return all_shows

    def get_percentage_of_all_availability(self) -> dict:
        """
        It returns a dictionary of all the shows in the theatre, with the percentage of available seats
        for each show.
        :return: A dictionary of the percentage of available seats for each show.
        """
        all_shows_perc = {}
        for show in self.shows:
            num_seats = len(show.seats)
            num_available_seats = show.get_number_of_all_available_seats()
            all_shows_perc[show.code] = round(
                num_available_seats / num_seats * 100, 2)
        return all_shows_perc

    def get_total_income(self) -> float:
        """
        This function takes in a list of shows and returns the total revenue of all the shows.
        :return: The total income of the theatre.
        """
        total_income = 0
        for show in self.shows:
            total_income += show.get_revenue()
        return total_income

    def get_best_selling_show(self) -> Tuple[List[Show], float]:
        """
        It loops through the shows in the list of shows, and if the revenue of the show is equal to the
        highest revenue, it adds the show to the list of best selling shows. If the revenue of the show
        is greater than the highest revenue, it clears the list of best selling shows, sets the highest
        revenue to the revenue of the show, and adds the show to the list of best selling shows
        :return: A tuple with a list of shows and a float.
        """
        list_with_best_selling_shows: List[Show] = []
        highest_revenue = 0
        for show in self.shows:
            revenue = show.get_revenue()
            if revenue == highest_revenue:
                list_with_best_selling_shows.append(show)
            if revenue > highest_revenue:
                list_with_best_selling_shows.clear()
                highest_revenue = revenue
                list_with_best_selling_shows.append(show)
        return list_with_best_selling_shows, highest_revenue

    def get_least_selling_show(self) -> Tuple[List[Show], float]:
        """
        It returns a list of shows with the least revenue and the least revenue itself
        :return: A tuple with a list of shows and a float.
        """
        list_with_least_selling_shows: List[Show] = []
        least_revenue = float("inf")
        for show in self.shows:
            revenue = show.get_revenue()
            if revenue == least_revenue:
                list_with_least_selling_shows.append(show)
            if revenue < least_revenue:
                list_with_least_selling_shows.clear()
                least_revenue = revenue
                list_with_least_selling_shows.append(show)
        return list_with_least_selling_shows, least_revenue

    def get_ticket_of_guest(self, name: str):
        """
        It takes a name as a parameter and returns a list of all the tickets that the user has bought.
        
        :param name: str = "John"
        :type name: str
        """
        bought_tickets: List[ShowSeat] = []
        for show in self.shows:
            for seat in show.seats:
                if seat.is_reserved and seat.guest_name == name:
                    show_seat = ShowSeat(show, seat)
                    bought_tickets.append(show_seat)
        if bought_tickets:
            show_seats_string = []
            for show_seat in bought_tickets:
                show_seat_string = f"{show_seat.seat} for show: {show_seat.show}"
                show_seats_string.append(show_seat_string)
            print("\n".join(show_seats_string))
        else:
            print(
                "Sorry, there are no tickets for this user. Try again with another name.")


class ShowSeat:
    show: Show
    seat: Seat

    def __init__(self, show: Show, seat: Seat) -> None:
        self. show = show
        self.seat = seat

    