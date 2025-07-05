class Match:
    def __init__(self, requester, volunteer):
        self.requester = requester
        self.volunteer = volunteer

    def get_match_info(self):
        return f"{self.requester.name} matched with {self.volunteer.name}"
