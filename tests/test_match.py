import unittest
from classes.user import User
from classes.match import Match

class TestMatch(unittest.TestCase):

    def test_match_creation(self):
        requester = User("Jarred", 21, "Manila", "Mechanic", "Diesel expert")
        volunteer = User("Raven", 22, "QC", "Mechanic", "Injector specialist")
        match = Match(requester, volunteer)

        self.assertEqual(match.requester.name, "Jarred")
        self.assertEqual(match.volunteer.name, "Raven")

    def test_get_match_info(self):
        requester = User("Ann", 23, "Cavite", "Electrician", "Power lines")
        volunteer = User("Jerica", 24, "Pasig", "Electrician", "Indoor wiring")
        match = Match(requester, volunteer)

        expected_output = "Ann matched with Jerica"
        self.assertEqual(match.get_match_info(), expected_output)

if __name__ == '__main__':
    unittest.main()
