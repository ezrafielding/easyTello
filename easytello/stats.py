from datetime import datetime

class Stats:
    def __init__(self, command: str, id: int):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response: str):
        self.response = response
        self.end_time = datetime.now()
        self.duration = (self.end_time-self.start_time).total_seconds()

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def get_response(self):
        return self.response

