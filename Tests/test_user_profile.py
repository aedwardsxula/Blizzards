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
        
    def test_sort_study_sessions(self):
        p = Profile("Lonzo", "CIS", "Math")

        now = datetime.now()
        s1 = StudySession(p, now + timedelta(hours=5), "Library", "Trees")
        s2 = StudySession(p, now + timedelta(hours=1), "STEM", "Loops")
        s3 = StudySession(p, now + timedelta(hours=3), "Dorm", "Graphs")

        p.schedule = [s1, s2, s3]

        sorted_sessions = p.sort_study_sessions()
        self.assertEqual(sorted_sessions, [s2, s3, s1])
        
    def test_upcoming_sessions(self):
        p = Profile("Lonzo", "CIS", "Math")

        now = datetime.now()
        past = StudySession(p, now - timedelta(hours=2), "Lab", "Past")
        today = StudySession(p, now, "Library", "Today")
        future = StudySession(p, now + timedelta(days=1), "Dorm", "Future")

        p.schedule = [past, today, future]

        result = p.upcoming_study_sessions(now)

        self.assertIn(today, result)
        self.assertIn(future, result)
        self.assertNotIn(past, result)
        
    def test_sort_empty_schedule(self):
        p = Profile("Lonzo", "CIS", "Math")
        self.assertEqual(p.sort_study_sessions(), [])
        
    def test_count_availability_by_hour(self):
        p1 = Profile("Sam", "CIS", "Math")
        p2 = Profile("Alex", "CE", "Physics")

        p1.schedule = [
            Event("Study", datetime(2025, 1, 1, 10, 0)),
            Event("Lab", datetime(2025, 1, 1, 14, 0))
        ]

        p2.schedule = [
            Event("Meeting", datetime(2025, 1, 1, 10, 30))
        ]

        counts = Profile.count_availability_by_hour([p1, p2])

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

    
if __name__ == '__main__':
    unittest.main()