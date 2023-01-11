from theatre import Theatre
from show import Show
from days_enum import DaysEnum
from seat_type_enum import SeatType


def modify_show_time(theatre: Theatre):
    """
    It takes a theatre object as an argument and asks the user to input a show code. It then uses the
    show code to find the show object and asks the user to input a new time for the show. It then
    changes the time of the show object (with the method change show time, from Show class) and prints the show object.

    :param theatre: Theatre
    :type theatre: Theatre
    """
    show = get_show_by_code_from_input(theatre)
    new_time = input("Insert a new time of a chosen show: ")
    show.change_show_time(new_time)
    print(show)


def remove_show_from_input(theatre: Theatre):
    """
    It removes a show from the theatre.

    :param theatre: Theatre
    :type theatre: Theatre
    """
    print_all_shows(theatre)
    show_str = input(
        "Insert the name of the show you would like to remove: ")
    show_to_remove = theatre.get_show_by_name(show_str)
    theatre.remove_show(show_to_remove)


def print_all_shows(theatre: Theatre):
    """
    It prints all the shows in the theatre. It is used 
    when proceeding with the ticket purchase from user input,
    so that the user can have an overview of all shows.  

    :param theatre: Theatre
    :type theatre: Theatre
    """
    print("Those are the available shows:")
    all_shows = theatre.get_all_shows()
    print("\n".join([str(show) for show in all_shows]))


def get_show_by_code_from_input(theatre: Theatre) -> Show:
    """
    It asks the user to input a show code, and if the code is not valid, it asks again until the user
    inputs a valid code.

    :param theatre: Theatre
    :type theatre: Theatre
    :return: The show object
    """
    print_all_shows(theatre)
    show_code = input(
        "Insert the code of the show: ")
    while not theatre.get_show_by_code(show_code):
        show_code = input(
            "Insert the code of the show: ")
    return theatre.get_show_by_code(show_code)


def get_show_seat_info(theatre: Theatre):
    """
    It gets a show from the theatre by asking the user for a show code, and then prints out the seats in
    that show

    :param theatre: Theatre
    :type theatre: Theatre
    """
    show = get_show_by_code_from_input(theatre)
    print("\n".join([str(seat) for seat in show.seats]))


def create_show_from_input():
    """
    It takes user input and creates a show object
    :return: the show1 object.
    """
    show_name = input("Insert the name of the show you would like to add: ")
    show_day = input(
        "Insert the day when the show is played from monday to sunday: ").upper()
    while show_day not in DaysEnum.__members__:
        show_day = input(
            "Insert the day when the show is played from monday to sunday: ").upper()
    show_day_enum = DaysEnum[show_day]
    show_time = input("Insert the time when the show starts: ")
    show_id = input("Insert the show code for the reservations: ")
    while True:
        try:
            vip_seat_price = float(input("Insert price for the VIP seats: "))
            break
        except ValueError:
            ("Please insert the correct value")
    while True:
        try:
            parter_seat_price = float(
                input("Inser price for the parter seats: "))
            break
        except ValueError:
            ("Please insert the correct value")

    show1 = Show(show_name, show_day_enum, show_time,
                 show_id, vip_seat_price, parter_seat_price)
    return show1


def create_theatre_from_input():
    """
    It creates a theatre object, adds two shows to it, and returns the theatre object. The shows added
    were mainly for the testing purposes.
    :return: the theatre object.
    """
    theatre_name = input("Insert the name of the theatre: ")
    theatre = Theatre(theatre_name)
    theatre.add_show(Show("Kad jaganjci utihnu", DaysEnum.FRIDAY,
                          "18", "kjufri18", 2000, 1000))
    theatre.add_show(Show("Bela kafa", DaysEnum.FRIDAY,
                          "19", "kafa19", 2000, 1000))
    return theatre


def get_ticket(theatre: Theatre):
    """
    It asks the user for a show code, a name, a number of tickets, and a seat type, and then it prints
    out the tickets that were bought
    
    :param theatre: Theatre
    :type theatre: Theatre
    """
    all_tickets = []
    choice1 = "yes"
    show = get_show_by_code_from_input(theatre)
    name = input("Insert your name: ")
    while choice1 != "no":
        while True:
            try:
                num_tickets = int(input("Insert the number of tickets "))
                break
            except ValueError:
                print("Please insert the correct value")
        seat = input("Insert VIP or PARTER: ").upper()
        while seat not in SeatType.__members__:
            seat = input("Insert VIP or PARTER:: ").upper()
        seat_enum = SeatType[seat]
        message, tickets = theatre.buy_tickets(
            show.code, num_tickets, name, seat_enum)
        if tickets:
            all_tickets += tickets
            print(f"Show for which tickets are boughts is: {show}")
            print(f"\n".join([str(seat) for seat in all_tickets]))
        else:
            print(message)
        choice1 = input(
            "Do you to buy more tickets for this show, if yes insert yes, if no insert no: ")
        while not choice1 == "yes" and not choice1 == "no":
            choice1 = input(
                "Do you to buy more tickets for this show, if yes insert yes, if no insert no: ")
    print(f"Show for which tickets are boughts is: {show}")
    print(f"\n".join([str(seat) for seat in all_tickets]))


def employee_menu(theatre: Theatre):
    print("To create a show, press a")
    print("To remove a show press b: ")
    print("To modify a show time, press c: ")
    print("To see the total availability of a thetre press d:")
    print("To see the availability in percentage, press e: ")
    print("To see the total income of shows, press f: ")
    print("To see the most selling show and the income of that show, press g: ")
    print("To see the least selling show and the income of that show, press h: ")
    print("To see all the seats of a show, press i: ")
    print("To go back to the main page insert q: ")
    while True:
        choice = input(
            "Insert one of the options from a to i, to go back to the main page insert q: ")
        if choice == "a":
            show = create_show_from_input()
            theatre.add_show(show)
        elif choice == "b":
            remove_show_from_input(theatre)
        elif choice == "c":
            modify_show_time(theatre)
        elif choice == "d":
            d = theatre.get_total_availability()
            for show_code, availability in d.items():
                print(
                    f"Show with the code {show_code} has {availability} seats.")
        elif choice == "e":
            e = theatre.get_percentage_of_all_availability()
            for show_code, percent in e.items():
                print(
                    f"Show with the code {show_code} has the availability of {percent} percents")
        elif choice == "f":
            f = theatre.get_total_income()
            print(f)
        elif choice == "g":
            list_with_best_selling_shows, highest_revenue = theatre.get_best_selling_show()
            if list_with_best_selling_shows:
                best_selling_string = []
                for best_show in list_with_best_selling_shows:
                    best_show_string = f"The best selling is {best_show.name} with revenue {highest_revenue}"
                    best_selling_string.append(best_show_string)
                print("\n".join(best_selling_string))
        elif choice == "h":
            list_with_least_selling_shows, least_revenue = theatre.get_least_selling_show()
            if list_with_least_selling_shows:
                least_selling_string = []
                for least_show in list_with_least_selling_shows:
                    least_show_string = f"The least selling is {least_show.name} with revenue {least_revenue}"
                    least_selling_string.append(least_show_string)
                print("\n".join(least_selling_string))
        elif choice == "i":
            get_show_seat_info(theatre)
        elif choice == "q":
            main_menu(theatre)
        else:
            print("Incorrect value, please enter values from a to i")


def guest_menu(theatre: Theatre):
    print("To see all the available shows in the theatre press a: ")
    print("To see the timetables of a desired show, press b: ")
    print("To check the prices of a desired show, press c: ")
    print("To proceed with the purchase, press d: ")
    print("To see all the bought tickets, press e: ")
    print("To go back to the main menu, press q: ")
    while True:
        choice = input(
            "Insert one of the options from a to d, to go back to the main page insert q: ")
        if choice == "a":
            print_all_shows(theatre)
        elif choice == "b":
            show_name = input(
                "Insert the name of the show you would like to see to see the timetables: ")
            while not theatre.get_show_by_name(show_name):
                show_name = input(
                    "Insert the name of the show you would like to see to see the timetables: ")
            b = theatre.get_show_timetable(show_name)
            for show in b:
                print(
                    f"Show: {show.name}, is played on: {show.day.name} at {show.time} with code {show.code}")
        elif choice == "c":
            show = get_show_by_code_from_input(theatre)
            c = show.get_ticket_price()
            for types, prices in c.items():
                print(f"{types} ticket costs {prices} ")
        elif choice == "d":
            get_ticket(theatre)
        elif choice == "e":
            name = input("Insert your name: ")
            theatre.get_ticket_of_guest(name)
        elif choice == "q":
            main_menu(theatre)


def main_menu(theatre: Theatre):
    menu_choice = input(
        "To log in as guest, press 1, to log in as employee, press 2, to quit the app press q: ")
    while menu_choice not in ["1", "2", "q"]:
        menu_choice = input(
            "To log in as guest, press 1, to log in as employee, press 2: ")
    if menu_choice == "1":
        guest_menu(theatre)
    elif menu_choice == "2":
        employee_menu(theatre)
    elif menu_choice == "q":
        quit()
    else:
        pass
