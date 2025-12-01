from event import Event
from study_session import StudySession
from datetime import datetime
class Profile:
    Valid_majors = {'CS', 'CIS', 'CE', 'BINF'}

    def __init__(self, id, first_name, last_name, major, schedule=None):
        self.id = int(id)
        self.first_name = first_name.title()
        self.last_name = last_name.title()

        # Validate major
        self.major = major.upper()
        if self.major not in self.Valid_majors:
            raise ValueError(
                f"Invalid major: {self.major}. Valid majors are: {', '.join(self.Valid_majors)}"
            )

        # Schedule begins empty unless provided
        self.schedule = schedule if schedule is not None else []

    def __str__(self):
    # Format schedule lines
        if not self.schedule:
            schedule_str = "  (no events scheduled)"
        else:
         schedule_str = "\n".join([f"  - {e}" for e in self.schedule])

        return (
        f"Profile:\n"
        f"  First Name: {self.first_name}\n"
        f"  Last Name: {self.last_name}\n"
        f"  Major: {self.major}\n"
        f"  Schedule:\n{schedule_str}"
    )

    def __repr__(self):
        return self.__str__()
    
    def _extract_datetime(self, item):
        """Return the datetime for Events / StudySessions / InviteLogic / AutoCancelJob."""
        if hasattr(item, "when"):
            return item.when
        if hasattr(item, "time"):
            return item.time
        return None

    def _has_datetime_conflict(self, dt: datetime):
        for item in self.schedule:
            item_dt = self._extract_datetime(item)
            if item_dt is not None and item_dt == dt:
                return True
        return False


    # Add event to schedule
    def add_event(self, event: Event):
        if event in self.schedule:
            return False  # Duplicate event reject
        if self._has_datetime_conflict(event.when):
            return False  # Datetime conflict reject
        self.schedule.append(event)
        return True

    # Remove all events matching the same "what"
    def remove_event(self, event: Event):
        before = len(self.schedule)
        self.schedule = [
            e for e in self.schedule
            if not (hasattr(e, "what") and e.what == event.what)
        ]
        return len(self.schedule) < before

    # Output events relative to a date
    def output_events(self, current_date: datetime | None = None):
        if current_date is None:
            current_date = datetime.now()

        output = []
        for item in self.schedule:
            dt = self._extract_datetime(item)
            if dt is None:
                continue

            if dt.date() < current_date.date():
                prefix = "LATE "
            elif dt.date() == current_date.date():
                prefix = "NOW "
            else:
                prefix = ""

            # Try to get a human-readable description
            if hasattr(item, "what"):
                label = item.what
            elif hasattr(item, "reason"):
                label = item.reason
            elif hasattr(item, "topic"):
                label = item.topic
            else:
                label = str(item)

            formatted_time = dt.strftime("%m/%d/%Y at %I:%M %p")
            output.append(f"{prefix}{label} at {formatted_time}")

        return output
    #sort events in reverse chronological order
    # Sort events by datetime in reverse chronological order
    def sort_events_reverse_chronological(self):
        self.schedule.sort(key=lambda e: e.when, reverse=True) 


    # Update an event at an index (no duplicate datetimes)
    def update_schedule_entry(self, index: int, event: Event):
        for existing in self.schedule:
            if existing.when == event.when:
                return False  # Duplicate datetime → reject
        if 0 <= index < len(self.schedule):
            self.schedule[index] = event
        return True

        return False  # Invalid index — do NOT update  

    # Change major safely
    def change_major(self, new_major: str):
        new_major = new_major.upper()
        if new_major in self.Valid_majors:
            self.major = new_major
            return True
        return False

    # Check for duplicate event times
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

