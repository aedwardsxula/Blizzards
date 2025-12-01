from mmp_driver import MMPDriver
import unittest
class TestMMPDriver(unittest.TestCase):
    def setUp(self):
        self.driver = MMPDriver()

    def test_random_name(self):
        name = self.driver.random_name()
        self.assertIsInstance(name, str)
        self.assertIn(",", name)

    def test_random_major(self):
        major = self.driver.random_major()
        self.assertIn(major, self.driver.MAJORS)

    def test_random_datetime(self):
        dt = self.driver.random_datetime()
        self.assertTrue(hasattr(dt, 'year'))
        self.assertTrue(hasattr(dt, 'month'))
        self.assertTrue(hasattr(dt, 'day'))

    def test_random_event(self):
        event = self.driver.random_event()
        self.assertTrue(hasattr(event, 'what'))
        self.assertTrue(hasattr(event, 'when'))

    def test_random_study_session(self):
        proposer = "Test Proposer"
        session = self.driver.random_study_session(proposer)
        self.assertEqual(session.proposer, proposer)
        self.assertTrue(hasattr(session, 'time'))
        self.assertTrue(hasattr(session, 'place'))
        self.assertTrue(hasattr(session, 'topic'))

    def test_random_111_profiles(self):
        profiles = self.driver.random_111_profiles()
        self.assertEqual(len(profiles), 111)
        for i, profile in enumerate(profiles, start=1):
            self.assertEqual(profile.id, i)
            self.assertIsInstance(profile.first_name, str)
            self.assertIsInstance(profile.last_name, str)
            self.assertIn(profile.major, self.driver.MAJORS)

if __name__ == "__main__":
    unittest.main()