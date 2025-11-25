from Blizzards.event import Event
from datetime import datetime
import unittest

class TestEvent(unittest.TestCase):

    def test_event_creation(self):
        event = Event("Meeting", datetime(2025, 12, 1, 14, 30))
        self.assertEqual(event.what, "Meeting")
        self.assertEqual(event.when, datetime(2025, 12, 1, 14, 30))

    def test_event_str(self):
        event = Event("Conference", datetime(2025, 12, 5, 9, 0))
        event_str = str(event)
        self.assertIn("Conference", event_str)
        self.assertIn("12/05/2025 at 09:00 AM", event_str)
        self.assertEqual(event_str, "Event: Conference at 12/05/2025 at 09:00 AM")

    def test_event_different_dates(self):
        event1 = Event("Workshop", datetime(2025, 11, 20, 10, 0))
        event2 = Event("Seminar", datetime(2025, 11, 21, 15, 30))
        self.assertEqual(event1.what, "Workshop")
        self.assertEqual(event2.what, "Seminar")
        self.assertNotEqual(event1.when, event2.when)
