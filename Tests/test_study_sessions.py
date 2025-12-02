import unittest
from datetime import datetime

from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from event import Event

class TestStudySessions(unittest.TestCase):

    # def test_remove_session_from_both_profiles(self):
    #     p1 = Profile("Sam", "CIS", "Math")
    #     p2 = Profile("Jamie", "Math", "CIS")

    #     s = StudySession(p1, "10AM", "Library", "Loops")

    #     p1.schedule.append(s)
    #     p2.schedule.append(s)

    #     removed = s.remove(p1, p2)

    #     self.assertTrue(removed)
    #     self.assertNotIn(s, p1.schedule)
    #     self.assertNotIn(s, p2.schedule)

    # def test_no_duplicate_datetime(self):
    #     p = Profile("Sam", "CIS", "Math")

    #     s1 = InviteLogic("Sam", "10AM", "Library", "Review")
    #     s2 = InviteLogic("Sam", "10AM", "Library", "Review Again")

    #     added1 = s1.add_to_profile(p)
    #     added2 = s2.add_to_profile(p)

    #     self.assertTrue(added1)
    #     self.assertFalse(added2)
    #     self.assertEqual(len(p.schedule), 1)

    pass
if __name__ == "__main__":
    unittest.main()
