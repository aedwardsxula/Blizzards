#TOdo 1 test user_profile.py creationCreate 
#TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
from event import Event
import unittest

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.Sam = Profile("Sam", "CIS", "Physics", "Unknown")

    def test_profile_creation_and_methods(self):
        #test constructor
        self.assertEqual(self.Sam.name, "Sam")
        self.assertEqual(self.Sam.major, "CIS")
        self.assertEqual(self.Sam.minor, "Physics")
        self.assertEqual(self.Sam.schedule, "Unknown")

    def test_update_schedule(self):
        self.Sam.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
        self.assertEqual(self.Sam.schedule, {"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
        self.assertIsInstance(self.Sam.schedule, dict)
        self.assertIn("Monday", self.Sam.schedule)
        self.assertEqual(self.Sam.schedule["Monday"], ["9AM", "2PM"])
        self.assertIn("Wednesday", self.Sam.schedule)
        self.assertEqual(self.Sam.schedule["Wednesday"], ["11AM"])

    def test_empty_schedule_update_and_modification(self):
        #Test empty schedule update
        self.Sam.update_schedule({})
        self.assertEqual(self.Sam.schedule, {})

    def test_profile_modification(self):
        #test constructor overwirtes old data
        self.Sam.name = "Samuel"
        self.assertEqual(self.Sam.name, "Samuel")
        self.Sam.major = "Math"
        self.assertEqual(self.Sam.major, "Math")
        self.Sam.minor = "Computer Science"
        self.assertEqual(self.Sam.minor, "Computer Science")    
    
    ###

    def test_profile_attributes(self):
        profile = Profile(1, "john", "doe", "cs")
        self.assertEqual(profile.id, 1)
        self.assertEqual(profile.first_name, "John")
        self.assertEqual(profile.last_name, "Doe")
        self.assertEqual(profile.major, "CS")
        self.assertEqual(profile.schedule, [])

    def test_update_schedule(self):
        profile = Profile(2, "jane", "smith", "cis")
        event = Event("Meeting", datetime(2024, 5, 20, 14, 0))
        profile.update_schedule(event)
        self.assertEqual(len(profile.schedule), 1)
        self.assertEqual(profile.schedule[0], event)

    def test_valid_datetime_in_event(self):
        event_date = datetime(2024, 6, 15, 10, 30)
        event = Event("Conference", event_date)
        self.assertIsInstance(event.event_date, datetime)

    def test_invalid_major_raises_value_error(self):
        with self.assertRaises(ValueError):
            Profile(3, "alice", "johnson", "math")

    def test_name_titlecase(self):
        profile = Profile(4, "michael", "brown", "ce")
        self.assertEqual(profile.first_name, "Michael")
        self.assertEqual(profile.last_name, "Brown")

if __name__ == '__main__':
    unittest.main()