#TOdo 1 test user_profile.py creationCreate 
# TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
Sam = Profile("Sam", "CIS", "Physics", "Unknown")

def test_profile_creation_and_methods():
    #test constructor
    assert Sam.name == "Sam"
    assert Sam.major == "CIS"
    assert Sam.minor == "Physics"
    assert Sam.schedule == "Unknown"

def test_update_schedule():
    Sam.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
    assert Sam.schedule == {"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]}
    assert isinstance(Sam.schedule, dict)
    assert "Monday" in Sam.schedule
    assert Sam.schedule["Monday"] == ["9AM", "2PM"]
    assert "Wednesday" in Sam.schedule
    assert Sam.schedule["Wednesday"] == ["11AM"]

def test_empty_schedule_update_and_modification():
    #Test empty schedule update
    Sam.update_schedule({})
    assert Sam.schedule == {}

def test_profile_modification():
    #test constructor overwirtes old data
    Sam.name = "Samuel"
    assert Sam.name == "Samuel"
    Sam.major = "Math"
    assert Sam.major == "Math"
    Sam.minor = "Computer Science"
    assert Sam.minor == "Computer Science"
