

import unittest 
from datetime import datetime
from user_profile import Profile

class Event:
    def __init__(self, name, event_date):
        self.name = name
        self.event_date = event_date

    def __repr__(self):
        return f"Event(name={self.name}, event_date={self.event_date})"

class TestProfile(unittest.TestCase):
    
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

  