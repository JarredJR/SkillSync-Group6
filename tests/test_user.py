import unittest
from classes.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("Jarred", 21, "Manila", "Mechanic", "Diesel expert")
        self.assertEqual(user.name, "Jarred")
        self.assertEqual(user.age, 21)
        self.assertEqual(user.specialization, "Mechanic")

    def test_user_string_output(self):
        user = User("Raven", 22, "QC", "Electrician", "Wiring and circuits")
        self.assertEqual(str(user), "Raven (Electrician) - Wiring and circuits")

if __name__ == '__main__':
    unittest.main()
