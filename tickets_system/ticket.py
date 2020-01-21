import time
import uuid


class Ticket:
    def __init__(self):
        self.id = uuid.uuid1()
        self.creation_timestamp = time.time()
