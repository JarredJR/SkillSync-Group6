class SkillRequest:
    def __init__(self, category, description, location, time):
        self.category = category
        self.description = description
        self.location = location
        self.time = time

    def is_valid(self):
        return all([self.category, self.description, self.location, self.time])

    def get_requester_info(self):
        return f"Request: {self.description} at {self.location} on {self.time}"
