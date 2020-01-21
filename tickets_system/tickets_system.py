from tickets_system.ticket import Ticket


class TicketsSystem:
    def __init__(self):
        self.valid_tickets = []

    def validate_ticket(self, ticket_id):
        output = list(filter(lambda ticket: ticket.id == ticket_id, self.valid_tickets))
        return len(output) != 0

    def invalidate_ticket(self, ticket_id):
        self.valid_tickets = list(filter(lambda ticket: ticket.id != ticket_id, self.valid_tickets))

    def add_ticket(self):
        new_ticket = Ticket()
        self.valid_tickets.append(new_ticket)
        return new_ticket

    def remove_ticket(self, ticket_id):
        self.invalidate_ticket(ticket_id)

