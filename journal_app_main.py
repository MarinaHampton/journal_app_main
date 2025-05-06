# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 04/30/2025
# Description:
# - Sprint 1 main program
# main menu
# get user choice
# wheel of emotions activity (open wheel_emotion.jpeg and enter emotion)
# save and load journal entries, and emotion tracker

from datetime import datetime
from ASCII_art import *
from morning_activities import *

# open wheel_emotion.jpeg
import subprocess
import platform
from pathlib import Path
# save and display past entries and emotions
import os
import json
from datetime import datetime

IMAGE_FOLDER_PATH = Path("/Users/marinahampton/PycharmProjects/journal_app_main")
IMAGE_FILENAME = "wheel_emotions.jpeg"
IMAGE_FULL_PATH = IMAGE_FOLDER_PATH / IMAGE_FILENAME

JOURNAL_FILE = "journal_entries.json"
EMOTION_FILE = "emotion_data.json"


def display_jump_to_menu():
    """Displays the menu to jump to a specific activity, grouped by time of day."""
    # print("\n--- Jump To A Specific Activity ---")
    print("Enter the number of the activity you want to access:")
    print("\n--- Morning Activities ---")
    print("1. Free write")
    print("2. View affirmations")
    print("3. Set daily goal")
    print("\n--- Evening Reflections ---")
    print("4. Reflect on challenges")
    print("5. Gratitude awareness")
    print("6. Needs awareness")
    print("\n--- History ---")
    print("7. View all entries")
    print("\n--- Other ---")
    print("8. Emotion Tracker")
    print("9. Return to Main Menu")
    print("10. Exit")
    print("-" * 40)

def get_jump_to_choice():
    """Gets the user's choice from the jump to menu."""
    while True:
        choice = input("Enter number (1-10)> ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

def jump_to_activity():
    """Handles the logic for jumping to a specific activity."""
    while True:
        display_jump_to_menu()
        jump_choice = get_jump_to_choice()

        if jump_choice == '1':
            print("\n--- Navigating to Free Write ---")
            free_write_activity()
        elif jump_choice == '2':
            print("\n--- Navigating to View Affirmations ---")
            #view_affirmations()
        elif jump_choice == '3':
            print("\n--- Navigating to Set Daily Goal ---")
            # set_daily_goal()
        elif jump_choice == '4':
            print("\n--- Navigating to Reflect on Challenges ---")
            #evening_reflections_menu()
        elif jump_choice == '5':
            print("\n--- Navigating to Gratitude Awareness ---")
            #evening_reflections_menu()
        elif jump_choice == '6':
            print("\n--- Navigating to Needs Awareness ---")
            #evening_reflections_menu()
        elif jump_choice == '7':
            print("\n--- Navigating to View All Entries ---")
            display_past_entries_and_emotions()
        elif jump_choice == '8':
            print("\n--- Navigating to Emotion Tracker ---")
            emotion_tracker_activity()
        elif jump_choice == '9':
            return # to the main menu
        elif jump_choice == '10':
            print("Exiting the Wellness Journal. Take care of yourself!")
            exit()
        else:
            print("Invalid choice. Please enter a number from the menu.")

def load_data(filename):
    """Loads data from a JSON file. Handles file not found and other errors."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File not found: {filename}. Returning an empty dataset.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {filename}.  Returning an empty dataset.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading data from {filename}: {e}")
        return []  # Return empty list to avoid crashing

def save_journal_entries(entries):
    """Saves the journal entries to the JSON file.Called after an entry is deleted."""
    filename = JOURNAL_FILE
    try:
        with open(filename, "w") as f:
            json.dump(entries, f, indent=4)
        print(f"Journal entries saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving journal entries: {e}")

def display_past_entries_and_emotions():
    """Displays a summary of past journal entries and emotions,
    allowing users to view and delete full entries by entering the entry number or date.
    Includes a prompt for user interaction.
    """
    journal_entries = load_data(JOURNAL_FILE)
    emotion_data = load_data(EMOTION_FILE)

    if not journal_entries and not emotion_data:
        print("No journal entries or emotion data available to display.")
        return

    emotions_by_date = {entry['date']: entry['emotion'] for entry in emotion_data}
    all_entries = []
    for entry in journal_entries:
        all_entries.append(entry)

    all_entries.sort(key=lambda x: x['date'], reverse=True)

    print("\n--- Journal Entry History ---")
    print("View details: Enter entry number or date.")
    print("Delete entry: Enter 'd' followed by the entry number.")
    print("Return to main menu: Enter 'm'.")
    print("-" * 70)
    print("{:<5} | {:<12} | {:<35} | {:<20}".format("#", "Date", "Journal Entry Snippet", "Emotion"))
    print("-" * 70)

    indexed_entries = {}
    for index, entry in enumerate(all_entries, 1):
        date = entry['date']
        snippet = "No entry"
        if entry['activity_type'] == 'morning_free_write':
            snippet = entry['entry'][:30] + "..." if len(entry['entry']) > 30 else entry['entry']
        else:
            snippet = f"{entry['activity_type'].title()} Entry"
        emotion = emotions_by_date.get(date, "No emotion")
        print("{:<5} | {:<12} | {:<35} | {:<20}".format(index, date, snippet, emotion))
        indexed_entries[str(index)] = {'date': date, 'entry': entry, 'original_index': journal_entries.index(entry)}
        if date not in indexed_entries:
            indexed_entries[date] = []
        indexed_entries[date].append({'index': index, 'entry': entry, 'original_index': journal_entries.index(entry)})

    print("-" * 70)

    while True:
        view_choice = input("\nEnter an entry number, date, 'd [number]' to delete, or 'm' for main menu:> ")
        if view_choice.lower() == 'm':
            return
        elif view_choice.lower().startswith('d '):
            try:
                delete_choice = view_choice.split(' ')[1]
                if delete_choice in indexed_entries:
                    entry_to_delete = indexed_entries[delete_choice]['entry']
                    print("\n--- Confirm Deletion ---")
                    print(f"Are you sure you want to delete the entry from {entry_to_delete['date']}?")
                    print("This action is permanent and cannot be undone.")
                    confirm = input("Enter 'yes' to delete or 'no' to cancel: ").lower()
                    if confirm == 'yes':
                        original_index_to_delete = indexed_entries[delete_choice]['original_index']
                        del journal_entries[original_index_to_delete]
                        save_journal_entries(journal_entries)
                        print("Entry deleted successfully.")
                        # Reload data to update the view
                        display_past_entries_and_emotions()
                        return
                    else:
                        print("Deletion cancelled.")
                else:
                    print("Invalid entry number to delete.")
            except IndexError:
                print("Invalid delete command. Use 'd' followed by the entry number (e.g., 'd 3').")
            except ValueError:
                print("Invalid entry number format.")
        elif view_choice in indexed_entries:
            selected_data = indexed_entries[view_choice]
            if isinstance(selected_data, list): # Handle cases with multiple entries on the same date
                date_to_view = selected_data[0]['entry']['date']
                print(f"\n--- Details for Entries on {date_to_view} ---")
                for item in selected_data:
                    entry_to_view = item['entry']
                    print(f"  Entry #{item['index']}")
                    print(f"  Date: {entry_to_view['date']}")
                    print(f"  Activity: {entry_to_view['activity_type'].title()}")
                    print(f"  Entry: {entry_to_view['entry']}")
                    emotion = emotions_by_date.get(date_to_view, "No emotion recorded")
                    print(f"  Emotion: {emotion}")
                    print("-" * 20)
            else:
                date_to_view = selected_data['date']
                entry_to_view = selected_data['entry']
                print(f"\n--- Details for Entry #{view_choice} on {date_to_view} ---")
                print(f"  Date: {entry_to_view['date']}")
                print(f"  Activity: {entry_to_view['activity_type'].title()}")
                print(f"  Entry: {entry_to_view['entry']}")
                emotion = emotions_by_date.get(date_to_view, "No emotion recorded")
                print(f"  Emotion: {emotion}")
                print("-" * 20)
            input("Press Enter to return to the journal entry history...")
        else:
            print("Invalid choice. Enter an entry number, date, 'd [number]' to delete, or 'm'.")

def display_main_menu():
    print("-----------| Wellness Journal |---------- ")
    #print(logo)
    print(logo_2)
    #print("__PLACEHOLDER FOR AN INSPO QUOTE MICROSERVICE?")
    date_time_now = datetime.now()
    date_time_to_display = date_time_now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"({date_time_to_display})")
    print("A space for your emotional and mental well being")
    print()
    print("Enter the number of your choice:")
    print()
    print("1. Enter Morning Activities")
    print("   - start your day with focused intention")
    print()
    print("2. Enter Evening Reflections")
    print("   - reflect on your day and cultivate gratitude")
    print()
    print("3. Emotion Tracker")
    print("   - track your current emotional state")
    print()
    print("4. View Past Entries and Emotions")
    print("   - view your personal journey over time, identify emotional patterns and gain")
    print("     valuable self-awareness")
    print()
    print("5. Jump To A Specific Activity")
    print("   - quickly access any of the journaling features")
    print()
    print("6. Exit")
    print("-" * 45)

def get_main_menu_choice():
    while True:
        choice = input("Enter your choice (1-5):> ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6")

def display_emotion_tracker_menu():
    print("\n----------| Emotion Tracking |----------")
    print("-------| How are you feeling ? |-------")
    print()
    print("Enter the number of your choice:")
    print("1. View \"Wheel of Emotions\"")
    print("2. Return to main menu")
    print("3. Enter emotion")
    print("-" * 45)

def get_emotion_tracker_choice():
    while True:
        choice = input("Enter number:> ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def open_image(filepath):
    try:
        filepath_str = str(filepath)
        if platform.system() == "Windows":
            subprocess.Popen(["start", filepath_str], shell=True)
        elif platform.system() == "Darwin": # macOS
            subprocess.Popen(["open", filepath_str])
        elif platform.system() == "Linux":
            subprocess.Popen(["xdg-open", filepath_str])
        else:
            print("Cannot automatically open image on your operating system.")
            print(f"Please open '{filepath_str}' manually.")
            return
        print(f"Attempting to open '{filepath_str}'...")
    except FileNotFoundError:
        print(f"Error: File '{filepath_str}' not found.")
    except Exception as e:
        print(f"An error occurred while trying to open the image: {e}")

def save_emotion(date, emotion):
    """Saves the user's emotion to the emotion data file."""
    filename = EMOTION_FILE
    new_emotion_entry = {
        "date": date,
        "emotion": emotion
    }
    emotions = load_data(filename)
    emotions.append(new_emotion_entry)
    try:
        with open(filename, "w") as f:
            json.dump(emotions, f, indent=4)
    except Exception as e:
        print(f"An error occurred while saving emotion data: {e}")

def emotion_tracker_activity():
    while True:
        display_emotion_tracker_menu()
        emotion_choice = get_emotion_tracker_choice()

        if emotion_choice == '1':
            print("\n--- Viewing \"Wheel of Emotions\" ---")
            open_image(IMAGE_FULL_PATH)
            input("Press Enter to return to Emotion Tracker menu...")
        elif emotion_choice == '2':
            return # to the main menu
        elif emotion_choice == '3':
            print("\n--- Entering Emotion ---")
            emotion_text = input("Enter your emotion: ")
            if not emotion_text.strip():
                print("\nNothing was entered. Tracking your emotions can provide valuable")
                print("insights into your well-being over time. Even a brief entry can be helpful.")
                input("Press Enter to continue...")
            else:
                print(f"You entered: {emotion_text}")
                print(f"Emotion saved successfully!")
                date = datetime.now().strftime("%Y-%m-%d")
                save_emotion(date, emotion_text)  # saving
        else:
            print("Invalid choice. Please enter a number from the menu.")



def main():
    while True:
        display_main_menu()
        user_choice = get_main_menu_choice()

        if user_choice == '1':
            print("\n--- Entering Morning Activities ---")
            morning_activities_menu()
            pass
        elif user_choice == '2':
            print("\n--- Entering Evening Reflections ---")
            # evening reflections
            pass
        elif user_choice == '3':
            print("\n--- Entering Emotion Tracker ---")
            emotion_tracker_activity()  # enter the emotion tracker activity

        elif user_choice == '4':
            print("\n--- Viewing Past Entries and Emotions ---")
            # viewing past entries
            display_past_entries_and_emotions()

        elif user_choice == '5':
            print("\n--- Jumping To A Specific Activity ---")
            jump_to_activity()
            pass
        elif user_choice == '6':
            print("Exiting the Wellness Journal. Take care of yourself!")
            break

if __name__ == "__main__":
    main()