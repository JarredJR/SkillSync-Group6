class User:
    def __init__(self, name, age, location, specialization, description):
        self.name = name
        self.age = age
        self.location = location
        self.specialization = specialization
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.specialization}) - {self.description}"

    def get_skills(self):
        return self.specialization

    def get_available_slots(self):
        return ["Monday 10AM", "Wednesday 3PM"]  # Placeholder
