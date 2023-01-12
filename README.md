# Tickets buying program

The classes are:
* Theatre
* Show
* Seat
* SeatType(Enum)
* DaysType(Enum)

The method for buying tickets is in the Theatre class, where it's checked if there are enough tickets for a requested show and seat type. If positive, method from the class Seat is referenced, and the seat will be booked there, under the guest's name. Further insight about the implementation of the methods is noted in method's documentation. 

## interactive_interface

When program is run from a main menu, it gives a user three opstions, 1 to log in as a guest, 2 to log in as an employee, and q is to get back to the main menu. 

Therefore, the main menu has the following structure: 

**main_menu** 
* 1: is for logging in as a guest.
* 2: is for logging in as an employee.
* q: quit the current interface mode (guest mode or employee mode.)

The program takes inputs from an employee of a theatre and from a guest. Therefore, there are three dedicated methods, *employee_menu*, *guest_menu* and *main_menu*. Users can switch to employee menu or guest menu through the main_menu by entering the letter q.

Logging in as a guest (option 1):

**guest_menu** has its options listed from a to e, and the last option, q, is to get back to the main menu. Options are:
* a: checking all the shows in a theatre.
* b: checking the timetables of a desired show. 
* c: checking the prices of a desired show. 
* d: proceeding with the purchase.
* e: checking all bought tickets of a certain user (by inserting the user's name).
* q: getting back to the main menu.

Logging in as an employee (option 2):

**employee_menu** has its options listed from a to i, and the last option, q, is to get back to the main menu. Options are:
* a: creating a new show.
* b: removing a show.
* c: modifying a show time(hours).
* d: getting the total availability of a theatre.
* e: getting the total availability in percentage.
* f: getting the total income of a theatre.
* g: getting the most selling show.
* h: getting the least selling show. 
* i: checking all the seats of a certain show. 
* q: getting back to the main menu.

In the interactive interface, there are as well other methods which are being used for implementing the employee menu and guest menu. 

You will notice as well that in the method `create_show_from_input`, where the shows were actually created without an input from a user, but it was implemented for the testing purposes.  




