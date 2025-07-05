class Availability:
    def __init__(self, user, time_slots):
        self.user = user
        self.time_slots = time_slots

    def is_available(self, time):
        return time in self.time_slots
