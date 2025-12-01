#TOdo 1 test user_profile.py creationCreate 
#TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
from event import Event
from study_session import StudySession
from datetime import datetime
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
###
class TestSortEvents(unittest.TestCase):

    def test_sort_events_basic(self):
        p = Profile(10, "john", "doe", "CS")

        e1 = Event("First", datetime(2024, 5, 20, 10, 0))
        e2 = Event("Second", datetime(2024, 5, 22, 9, 0))
        e3 = Event("Third", datetime(2024, 5, 21, 15, 0))

        p.schedule.extend([e1, e2, e3])
        p.sort_events()

        self.assertEqual(p.schedule, [e2, e3, e1])

    def test_sort_events_with_study_session(self):
        p = Profile(11, "amy", "smith", "CIS")

        e1 = Event("Old Event", datetime(2024, 4, 10, 10, 0))
        s1 = StudySession("Amy", datetime(2024, 4, 12, 14, 30), "Library", "Review")
        e2 = Event("Newest Event", datetime(2024, 4, 15, 9, 0))

        p.schedule.extend([e1, s1, e2])
        p.sort_events()

        # Newest → oldest
        self.assertEqual(p.schedule, [e2, s1, e1])

        self.assertEqual(counts[10], 2)
        self.assertEqual(counts[14], 1)
        
    def test_best_hour(self):
        data = {10: 3, 8: 3, 14: 1}
        self.assertEqual(Profile.best_hour(data), 8)
        
    def test_best_hour_empty(self):
        self.assertIsNone(Profile.best_hour({}))
        
    def test_event_vs_event_conflict(self):
        p = Profile("Sam", "CIS", "Math")
        e1 = Event("Study", datetime(2025, 1, 1, 10, 0))
        e2 = Event("Lab", datetime(2025, 1, 1, 10, 0))

        p.schedule = [e1]
        self.assertTrue(p.has_conflict(e2))
        
    def test_session_vs_session_conflict(self):
        p = Profile("Sam", "CIS", "Math")
        s1 = StudySession(p, datetime(2025, 1, 1, 18, 0), "STEM", "Loops")
        s2 = StudySession(p, datetime(2025, 1, 1, 18, 0), "Dorm", "Graphs")

        p.schedule = [s1]
        self.assertTrue(p.has_conflict(s2))
        
    def test_add_study_session_success(self):
        p = Profile("Sam", "CIS", "Math")
        s1 = StudySession(p, datetime(2025, 1, 2, 12, 0), "STEM", "Loops")

        added = p.add_study_session(s1)
        self.assertTrue(added)
        self.assertIn(s1, p.schedule)
        
    def test_add_study_session_fail_on_conflict(self):
        p = Profile("Sam", "CIS", "Math")
        s1 = StudySession(p, datetime(2025, 1, 2, 12, 0), "STEM", "Loops")
        s2 = StudySession(p, datetime(2025, 1, 2, 12, 0), "Library", "Trees")

        p.schedule = [s1]
        added = p.add_study_session(s2)

        self.assertFalse(added)
        self.assertEqual(len(p.schedule), 1)

    
if __name__ == '__main__':
    unittest.main()