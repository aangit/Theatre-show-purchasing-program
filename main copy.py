from theatre import Theatre
from show import Show
from days_enum import DaysEnum
from seat_type_enum import SeatType

if __name__ == "__main__":
    theatre1 = Theatre("Vuk")
    show1 = Show("Kad jaganjci utihnu", DaysEnum.MONDAY,
                 "17", "kjumon17", 1500, 1000)
    show2 = Show("Kad jaganjci utihnu", DaysEnum.FRIDAY,
                 "18", "kjufri18", 2000, 1000)
    # print(show1.seats)
    # print(show1.seats)
    # print("Number of VIP seats: ")
    # print(show1.number_of_available_seats(SeatType.VIP))
    # print("Number of parter seats: ")
    # print(show1.number_of_available_seats(SeatType.PARTER))
    # print("Check if VIP available: ")
    # print(show1.check_available_seats(6, SeatType.VIP))
    # print("Check if parter available: ")
    # print(show1.check_available_seats(4, SeatType.PARTER))
    theatre1.add_show(show1)
    theatre1.add_show(show2)
    # print(theatre1.shows)

    # print("Show timetable")
    # # print(theatre1.get_show_timetable("Kad jaganjci utihnu"))
    ticket = theatre1.buy_tickets("kjumon17", 17, "Andjela", SeatType.PARTER)
    ticket2 = theatre1.buy_tickets("kjumon17", 60, "Nikola", SeatType.VIP)
    # ticket3 = theatre1.buy_tickets("kjumon17", 148, "Matija" , SeatType.PARTER)
    print(show1.number_of_available_seats(SeatType.VIP))
    print(show1.number_of_available_seats(SeatType.PARTER))

    # ticket4= theatre1.buy_tickets("kjumon17", 60, "Nikola", SeatType.VIP)
    # print(ticket2)
    # print(ticket4)
    # ticket3 = theatre1.buy_tickets("kjumon17", 148, "Andjela", SeatType.PARTER)
    # ticket3 = theatre1.buy_tickets("kjumon17", 20, "Andjela", SeatType.PARTER)
    # ticket3 = theatre1.buy_tickets("kjufri18", 5, "Mirko", SeatType.VIP)
    # # print(ticket)

    # print(theatre1.get_show_availability(SeatType.VIP))
    # print(theatre1.get_percentage_of_availability(SeatType.VIP))
    # print(theatre1.get_total_income())
    print(theatre1.get_best_selling_show())
    print(theatre1.get_least_selling_show())
    # print(theatre1.get_total_availability())
    # print(theatre1.get_percentage_of_all_availability())

    # all_shows = " "
    # see_timetabes = " "
    # check_prices = " "
    # show_code = " "
    # num_tickets = " "
    # name = " "
    # seat = " "
    # while all_shows != "end" and see_timetabes != "end" and check_prices != "end" and show_code != "end" and num_tickets != "end" and name != "end" and seat != "end":
    # all_shows = input(
    #     "To see all available shows in this theatre, insert 1 ")
    # while all_shows != "1":
    #     all_shows = input(
    #         "To see all available shows in this theatre, insert 1 ")
    # print(theatre1.get_all_shows())

    # see_timetabes = input(
    #     "Insert the name of the show you would like to see to see the timetables: ")
    # while not theatre1.get_show_by_name(see_timetabes):
    #     see_timetabes = input(
    #         "Insert the name of the show you would like to see to see the timetables: ")
    # print(theatre1.get_show_timetable(see_timetabes))

    # check_prices = input(
    #     "To chech the prices for the show, insert show code: ")
    # while not theatre1.get_show_by_code(check_prices):
    #     check_prices = input(
    #         "To chech the prices for the show, insert show code: ")
    # print(theatre1.get_ticket_price(check_prices))
    # print("to proceed with the purchace, we would need the following information: ")
    # show_code = input("Insert the show code ")
    # while not theatre1.get_show_by_code(show_code):
    #     show_code = input("Insert the show code ")

    # while True:
    #     try:
    #         num_tickets = int(input("Insert the number of tickets "))
    #         break
    #     except ValueError:
    #         ("Please insert the correct value")

    # name = input("Insert your name: ")
    # seat = input("for VIP insert 1 and for PARTER insert 2: ")
    # while not seat == "1" and not seat == "2":
    #     seat = input("for VIP insert 1 and for PARTER insert 2: ")
    # if seat == "1":
    #     ticket = theatre1.buy_tickets(
    #         show_code, num_tickets, name, SeatType.VIP)
    #     print(ticket)
    # elif seat == "2":
    #     ticket = theatre1.buy_tickets(
    #         show_code, num_tickets, name, SeatType.PARTER)
    #     print(ticket)
    
    # print(show1.number_of_available_seats(SeatType.VIP))
    # print(show1.number_of_available_seats(SeatType.PARTER))

    # try:
    #     theatre1.buy_tickets("kjufri18", 2, "Sanja")
    # except ValueError as e:
    #     alternatives = e.args[0]
    #     print("The selected show is sold out. Here below are the available options:")
    #     for i, alt in enumerate(alternatives):
    #         print(f"{i+1}. {alternatives.name}")


#da napravim da moze da pogleda za sledeci termin ako nema iz elifa za drugi tip 
#da sredim elif
#podeliti u visa fja, i onda njih pozivati