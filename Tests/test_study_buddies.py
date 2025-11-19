import pytest
from datetime import datetime, timedelta

from profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator


# Test: profile creation
def test_profile_creation():
    p = Profile(name="Lonzo", major="CIS", minor="Business")
    assert p.name == "Lonzo"
    assert p.major == "CIS"
    assert p.minor == "Business"
    assert isinstance(p.schedule, dict) or p.schedule is None


# Test: Schedule updates persist
def test_schedule_updates_persist():
    p = Profile("Lonzo", "CIS", "Business")
    new_schedule = {"Monday": ["10AM", "1PM"], "Wednesday": ["2PM"]}
    p.update_schedule(new_schedule)
    assert p.schedule == new_schedule


# Test: session proposals store time/place/topic
def test_session_proposal_stores_details():
    s = StudySession(
        proposer="Lonzo",
        time="3PM",
        place="Library",
        topic="Review Chapter 3",
        status="pending"
    )
    assert s.time == "3PM"
    assert s.place == "Library"
    assert s.topic == "Review Chapter 3"
    assert s.status == "pending"


# Test: decline
def test_decline_invitation():
    sess = InviteLogic(
        proposer="Lonzo",
        time="6PM",
        place="STEM Building",
        topic="Homework 4",
        status="pending"
    )
    declined = sess.decline_invite()
    assert declined is True
    assert sess.status == "declined"


# Test: Pending session autocancels after X hours
def test_pending_session_auto_cancel_after_hours():
    start_time = datetime.now() - timedelta(hours=4)
    sess = AutoCancelJob(
        proposer="Lonzo",
        time=start_time,
        place="Library",
        topic="Quiz Review",
        status="pending",
        cancel_after_hours=3
    )
    was_cancelled = sess.auto_cancel(current_time=datetime.now())
    assert was_cancelled is True
    assert sess.status == "cancelled"


# Test: cancellation notifications
def test_cancellation_notifications_sent():
    sess = AutoCancelJob(
        proposer="Lonzo",
        time=datetime.now() - timedelta(hours=4),
        place="Library",
        topic="Algorithm Review",
        status="pending",
        cancel_after_hours=3
    )
    buddies = ["buddy1@xula.edu", "buddy2@xula.edu"]
    notifications = sess.notify_buddies(buddies)
    assert len(notifications) == 2
    assert "buddy1@xula.edu" in notifications[0]
    assert "cancelled" in notifications[0].lower()


# Test: flashcards generate only for topics in DATE1..DATE2
def test_flashcards_generate_for_correct_date_range():
    syllabus = [
        {"topic": "Intro to CS", "date": datetime(2024, 9, 1)},
        {"topic": "Python Loops", "date": datetime(2024, 9, 10)},
        {"topic": "Recursion", "date": datetime(2024, 9, 20)},
        {"topic": "Trees", "date": datetime(2024, 10, 1)}
    ]

    generator = FlashcardGenerator(syllabus)
    start = datetime(2024, 9, 5)
    end = datetime(2024, 9, 25)

    cards = generator.generate(start, end)
    topics = [c["topic"] for c in cards]

    assert "Intro to CS" not in topics
    assert "Trees" not in topics
    assert "Python Loops" in topics
    assert "Recursion" in topics
