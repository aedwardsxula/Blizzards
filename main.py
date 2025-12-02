from datetime import datetime, timedelta
from py_compile import main
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator
from event import Event
import random

def print_welcome_banner():
    banner = r"""
    ================================================
    __        __   _                            _         
    \ \      / /__| | ___ ___  _ __ ___   ___  | |   
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |_|   
      \ V  V /  __/ | (_| (_) | | | | | |  __/  _ 
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|

    ________________________________________________
    
    Welcome to Study Buddies — let us learn together!
    ________________________________________________
    ================================================
    """
    print(banner)

while True:
        print("\n==================== STUDY BUDDY APP ====================")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. List All Profiles")
        print("4. Change Major")
        print("5. Add Event")
        print("6. Remove Event")
        print("7. Sort Events")
        print("8. View Events")
        print("9. Create and Invite Study Session")
        print("10. Accept Invite")
        print("11. Decline Invite")
        print("12. Auto-Cancel Session")
        print("13. Remove Study Session From Both Profiles")
        print("14. Exit")

        choice = input("Select option: ").strip()

        if choice == "1": create_profile()
        elif choice == "2": view_profile()
        elif choice == "3": list_profiles()
        elif choice == "4": change_major()
        elif choice == "5": add_event()
        elif choice == "6": remove_event()
        elif choice == "7": sort_events()
        elif choice == "8": view_events()
        elif choice == "9": invite_two_profiles()
        elif choice == "10": accept_invite()
        elif choice == "11": decline_invite()
        elif choice == "12": auto_cancel_session()
        elif choice == "13": remove_session_from_both()
        elif choice == "14":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")

print("\nDriver ended")






if __name__ == "__main__":
        main()