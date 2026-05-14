from abc import ABC, abstractmethod
class Seat(ABC):
    def __init__(self,viewer):
        self.viewer = viewer
    @abstractmethod
    def ticket_price(self):
        pass
class Standard(Seat):
    def ticket_price(self):
        return 35_000
class Premium(Seat):
    def ticket_price(self):
        return 70_000
class Vip(Seat):
    def ticket_price(self):
        return 120_000
class TicketSystem:
    def __init__(self):
        self.bookings = [] 

    def add(self,seat: Seat):
        self.bookings.append(seat)
class Ticket(ABC):
    @abstractmethod
    def print_ticket(self,bookings):
        pass
class PaperTicket(Ticket):
    def print_ticket(self,bookings):
        for seat in bookings:
            print(f"TICKET <{seat.viewer}> price={seat.ticket_price()}")
class QrSender(ABC):
    @abstractmethod
    def send(self,bookings):
        pass
class TelegramQrSender(QrSender):
    def send(self,bookings):
        for seat in bookings:
            print(f"[QR → {seat.viewer}] Show this at entrance. Paid {seat.ticket_price()} so'm")
class TicketSystem:
    def __init__(self):
        self.bookings = []

    def add(self, seat: Seat):
        self.bookings.append(seat)

    def run(self, ticket_printer, qr_sender):
        ticket_printer.print_ticket(self.bookings)
        qr_sender.send(self.bookings)
