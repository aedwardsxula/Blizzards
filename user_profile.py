# Implement Profile Class
#Attributes: name, major, minor, schedule
#Methods: update_schedule()

#Create a Profile class that has attributes: id(int), first_name(str), last_name(str), schedule(list[Event]), major(str).  
# Create a constructor and a __str__ method.  The first and last names must be formatted in Titlecase.  
# The major must be formatted in TITLECASE.  The schedule must begin as an empty list.
from typing import Optional, List
from event import Event
from study_session import StudySession
from datetime import datetime
class Profile:
    valid_majors = {'CS', 'CIS', 'CE', 'CE', 'BINF'}

    def __init__(self, id: int, first_name: str, last_name: str, major: str, schedule: Optional[List[Event]] = None):
        self.id = int(id)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.major = major.upper()
        if self.major not in self.valid_majors:
            raise ValueError(f"Invalid major: {self.major}. Valid majors are: {', '.join(self.valid_majors)}")
        self.schedule = schedule if schedule is not None else []

    def append_event_to_schedule(self, event: Event):
        self.schedule.append(event)

    

    def __str__(self):
        return f"Profile(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, major={self.major}, schedule={self.schedule})"

    def sort_events(self):
        """
        Sort the events in the schedule in reverse chronological order.
        Newest → Oldest.
        """
        # Some schedule items may be Event objects, others StudySession objects
        # So we must check whether they have attribute "when" or "time"
        def get_datetime(item):
            if hasattr(item, "when"):
                return item.when
            if hasattr(item, "time"):
                return item.time
            return datetime.min  # fallback to keep unknown items at the bottom

        self.schedule.sort(key=get_datetime, reverse=True)















# class Profile:
#     def __init__(self, name, major, minor, schedule=None):
#         self.name = name
#         self.major = major
#         self.minor = minor
#         self.schedule = schedule if schedule is not None else []

#     def update_schedule(self, new_schedule):
#         self.schedule = new_schedule

    def __repr__(self):
        return f"Name: {self.name } \nMajor: {self.major} | Minor: {self.minor} \nSchedule: {self.schedule}"
    
    # Create a remove_event method that removes all events in 
    # the schedule that have the same what attribute as the given event.
    def remove_event(self, event: Event):
        before = len(self.schedule)
        self.schedule = [e for e in self.schedule if e.what != event.what]
        return len(self.schedule) < before
    
    # Create an output_events method that outputs the event in a given Profile object.
    def output_events(self, current_date: datetime):
        output = []

        for e in self.schedule:
            if e.when.date() < current_date.date():
                prefix = "LATE "
            elif e.when.date() == current_date.date():
                prefix = "NOW "
            else:
                prefix = ""

            formatted_time = e.when.strftime("%m/%d/%Y at %I:%M %p")
            output.append(f"{prefix}{e.what} at {formatted_time}")

        return output

    # NEW: update a single schedule entry with an Event
    def update_schedule(self, index: int, event: Event):
        if 0 <= index < len(self.schedule):
            self.schedule[index] = event
            return True
        return False


    # NEW: change major
    def change_major(self, new_major: str):
        self.major = new_major

    # To help with testing: ensure no duplicate events
    def has_duplicate_events(self):
        seen = set()
        for e in self.schedule:
            if e.when in seen:
                return True
            seen.add(e.when)
        return False
    # Sort Study Sessions Earliest → Latest
    def sort_study_sessions(self):
        if not hasattr(self, "schedule") or len(self.schedule) == 0:
            return []
        return sorted(self.schedule, key=lambda session: session.time)
    
    # Filter Only Upcoming Sessions
    def upcoming_study_sessions(self, current_time=None):
        if current_time is None:
            current_time = datetime.now()

        upcoming = [
            session for session in self.schedule
            if session.time >= current_time
        ]
        return sorted(upcoming, key=lambda s: s.time)
    
    @staticmethod
    def count_availability_by_hour(profiles):
        hour_counts = {}

        for profile in profiles:
            for event in profile.schedule:
                hour = event.when.hour

                # If hour not in dictionary yet, start at 0
                if hour not in hour_counts:
                    hour_counts[hour] = 0

                # Increase count
                hour_counts[hour] += 1

        return hour_counts
    
    @staticmethod
    def best_hour(hour_dict):
        if len(hour_dict) == 0:
            return None

        # Start with the first hour in the dictionary
        best_hour = None
        best_value = -1

        for hour in hour_dict:
            count = hour_dict[hour]

            # If count is higher OR same count but earlier hour
            if count > best_value or (count == best_value and (best_hour is None or hour < best_hour)):
                best_hour = hour
                best_value = count

        return best_hour
    
    def has_conflict(self, new_session):
        for item in self.schedule:
            if item.when == new_session.when:
                return True
        return False
    
    def add_study_session(self, new_session):
        if self.has_conflict(new_session):
            return False

        self.schedule.append(new_session)
        return True

