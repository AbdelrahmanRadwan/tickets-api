import time
import uuid


class Ticket:
    def __init__(self):
        self.id = uuid.uuid1()
        self.creation_timestamp = time.time()
        self.valid = True

    def to_json(self):
        return {
            "id": self.id,
            "valid": self.valid,
            "timestamp": self.creation_timestamp
        }
