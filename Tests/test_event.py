from event import Event
from datetime import datetime

def test_event_creation():
    event = Event("Meeting", datetime(2025, 12, 1, 14, 30))
    assert event.what == "Meeting"
    assert event.when == datetime(2025, 12, 1, 14, 30)

def test_event_str():
    event = Event("Conference", datetime(2025, 12, 5, 9, 0))
    event_str = str(event)
    assert "Conference" in event_str
    assert "12/05/2025 at 09:00 AM" in event_str
    assert event_str == "Event: Conference at 12/05/2025 at 09:00 AM"

def test_event_different_dates():
    event1 = Event("Workshop", datetime(2025, 11, 20, 10, 0))
    event2 = Event("Seminar", datetime(2025, 11, 21, 15, 30))
    assert event1.what == "Workshop"
    assert event2.what == "Seminar"
    assert event1.when != event2.when