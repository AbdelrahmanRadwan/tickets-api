from unittest import TestCase
from tickets_system.tickets_system import TicketsSystem


class TestScoringPersonalList(TestCase):

    def test_add_validate_remove_tickets(self):
        tickets_system = TicketsSystem()
        # Try to add a ticket and check if it is added or not
        added_ticket = tickets_system.add_ticket()
        self.assertEqual(tickets_system.valid_tickets[0].id, added_ticket.id)
        # validate the added ticket
        self.assertEqual(tickets_system.validate_ticket(added_ticket.id), True)
        # invalidate the ticket and check again
        tickets_system.invalidate_ticket(added_ticket.id)
        self.assertEqual(tickets_system.validate_ticket(added_ticket.id), False)


