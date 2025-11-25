from event import Event
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


    # Add event to schedule
    def add_event(self, event: Event):
        self.schedule.append(event)

    # Remove all events matching the same "what"
    def remove_event(self, event: Event):
        before = len(self.schedule)
        self.schedule = [e for e in self.schedule if e.what != event.what]
        return len(self.schedule) < before

    # Output events relative to a date
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
