from tickets_system.ticket import Ticket


class TicketsSystem:
    def __init__(self):
        self.tickets = {}

    def get_ticket(self, ticket_id):
        if ticket_id:
            return list(self.tickets[ticket_id].to_json())
        else:
            return list(self.tickets)

    def add_ticket(self):
        new_ticket = Ticket()
        self.tickets[str(new_ticket.id)] = new_ticket
        return new_ticket.to_json()

    def validate_ticket(self, ticket_id):
        ticket_id = str(ticket_id)
        if ticket_id in self.tickets:
            self.tickets[ticket_id].valid = True
            return self.tickets[ticket_id].to_json()
        else:
            return {}

    def invalidate_ticket(self, ticket_id):
        ticket_id = str(ticket_id)
        if ticket_id in self.tickets:
            self.tickets[ticket_id].valid = False
            return self.tickets[ticket_id].to_json()
        else:
            return {}


