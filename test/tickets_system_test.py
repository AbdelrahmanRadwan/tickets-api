from unittest import TestCase
from tickets_system.tickets_system import TicketsSystem


class TestTicketsSystem(TestCase):

    def test_add_validate_invalidate_tickets(self):
        tickets_system = TicketsSystem()
        # Try to add a ticket and check if it is added or not
        added_ticket = tickets_system.add_ticket()
        ticked_id = str(added_ticket["id"])
        self.assertEqual(str(tickets_system.tickets[ticked_id].id), ticked_id)
        # validate the added ticket
        self.assertEqual(tickets_system.validate_ticket(ticked_id)["valid"], True)
        # invalidate the ticket and check again
        self.assertEqual(tickets_system.invalidate_ticket(ticked_id)["valid"], False)


