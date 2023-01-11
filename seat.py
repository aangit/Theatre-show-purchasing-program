from seat_type_enum import SeatType


class Seat:
    seat_number: int
    price: float
    is_reserved: bool
    guest_name: str
    row: int
    seat_type: SeatType

    def __init__(self, seat_number: int, row: int, seat_type: SeatType, price: float):
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.price = price
        self.row = row
        self.is_reserved = False

    def __str__(self) -> str:

        if self.is_reserved:
            return f"Seat number: {self.seat_number} is booked by {self.guest_name} and costs {self.price} in row {self.row}"
        else:
            return f"Seat in row {self.row} number {self.seat_number} type {self.seat_type.name} price {self.price} is not reserved."
            

    def __repr__(self) -> str:
        if self.is_reserved:
            return f"Seat number: {self.seat_number} is booked by {self.guest_name} and costs {self.price} in row {self.row} "
        else:
            return f"Seat in row {self.row} number {self.seat_number} type {self.seat_type.name} price {self.price} is not reserved."

    def book_seat(self, name: str):
        if not self.is_reserved:
            self.is_reserved = True
            self.guest_name = name
