# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 04/30/2025
# Description: morning_activities.py
# includes "morning activities" for journal app
# free_write_activity
# save and load free write data

from datetime import datetime
import random
import json

JOURNAL_FILE = "journal_entries.json"

def display_morning_menu():
    """Displays the menu for morning activities."""
    now = datetime.now()
    current_time = now.strftime("%a %b %d %I:%M%p") # e.g., "Wed May 06 09:03AM"
    print("\n----------| Morning Activities |----------")
    print(f"[{current_time}]")
    print("Set your intentions for the day ahead.")
    print("\nEnter the number of your choice:")
    print("1. Free write")
    print("   - express yourself in words")
    print()
    print("2. View affirmations")
    print("   - cultivate positive thoughts")
    print()
    print("3. Set daily goal")
    print("   - write down your highest priority goal for today")
    print()
    print("4. Return to main menu")
    print()
    print("5. Exit")
    print()
    print("-" * 45)

def get_morning_menu_choice():
    while True:
        choice = input("Enter your choice (1-5):> ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def morning_activities_menu():
    """Handles the logic for the morning activities menu."""
    while True:
        display_morning_menu()
        morning_choice = get_morning_menu_choice()

        if morning_choice == '1':
            #print("\n--- Free Write ---")
            free_write_activity()
        elif morning_choice == '2':
            print("\n--- View Affirmations ---")
            # view_affirmations()
        elif morning_choice == '3':
            print("\n--- Set Daily Goal ---")
            # set_daily_goal()
        elif morning_choice == '4':
            return # Return to the main menu
        elif morning_choice == '5':
            print("Exiting the Wellness Journal. Take care of yourself!")
            exit()
        else:
            print("Invalid choice. Please enter a number from the menu.")


def get_writing_prompt():
    prompts = [
        "What are you grateful for today?",
        "Describe a small act of kindness you witnessed or performed.",
        "What is a goal you have for the week and why is it important to you?",
        "Write about a place where you feel completely at peace.",
        "What is a challenge you are currently facing and how are you approaching it?",
        "Describe a memory that makes you smile.",
        "What is something you want to learn or explore?",
        "If you could have a conversation with anyone (living or deceased), who would it be and what would you talk about?",
        "What is a small step you can take today to improve your well-being?"
        "If you could give your younger self one piece of advice, what would it be and why?"
        "Who or what has had the biggest positive impact on your life?"
        "What are you most afraid of?"
    ]
    return random.choice(prompts)


def free_write_activity():
    print("\n--- Morning Free Write ---")
    print("Use the space below to express yourself.")
    print("Feeling uninspired? Enter PROMPT on a new line for a writing prompt")
    print("Type 'DONE' on a new line to save and exit.")
    print("-" * 40)

    lines = []
    word_count = 0
    prompt = None
    while True:
        line = input(f" FREE WRITE ({word_count} words)> ")
        if line.upper() == 'DONE':
            print(f"\nEntry saved successfully!")
            break
        elif line.upper() == 'PROMPT':
            prompt = get_writing_prompt()  # Store the prompt
            print(f"\nPROMPT: {prompt}\n")
        else:
            words_in_line = line.split()
            word_count += len(words_in_line)
            lines.append(line)
            if word_count >= 500:
                print("\n Congrats! You've written 500 words!")

    if lines:
        entry_content = "\n".join(lines)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_journal_entry(timestamp, entry_content, "morning_free_write", prompt)  # Pass prompt
        print(f"\nEntry saved at {timestamp}")
    else:
        print("\nNo entry written.")

    input("Press Enter to return to the morning activities menu...")

def save_journal_entry(timestamp, content, activity_type, prompt=None): # added prompt parameter
    """Saves journal entry data to a JSON file, including timestamp, activity type, and prompt."""
    filename = JOURNAL_FILE  # Use the constant defined at the beginning
    new_entry = {
        "timestamp": timestamp,
        "activity_type": activity_type,
        "entry": content,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "prompt": prompt  # Include the prompt in the saved data
    }

    # Load existing entries, append the new one, and save
    entries = load_data(filename)  # changed to use load_data()
    entries.append(new_entry)

    try:
        with open(filename, "w") as f:
            json.dump(entries, f, indent=4)  # Use json.dump for JSON formatting
    except Exception as e:
        print(f"An error occurred while saving the journal entry to {filename}: {e}")

def load_data(filename): #added load_data() here to be used in this file
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