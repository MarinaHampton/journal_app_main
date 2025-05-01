# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 04/30/2025
# Description:
# - Sprint 1 main program
# main menu
# get user choice
# wheel of emotions activity (open wheel_emotion.jpeg and enter emotion)

from datetime import datetime
from ASCII_art import *
from morning_activities import *

# open wheel_emotion.jpeg
import subprocess
import platform
from pathlib import Path

IMAGE_FOLDER_PATH = Path("/Users/marinahampton/PycharmProjects/journal_app_main")
IMAGE_FILENAME = "wheel_emotions.jpeg"
IMAGE_FULL_PATH = IMAGE_FOLDER_PATH / IMAGE_FILENAME


def display_main_menu():
    print("-----------| Wellness Journal |---------- ")
    #print(logo)
    print(logo_2)
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
            print(f"You entered: {emotion_text}")
            input("Press Enter to return to Emotion Tracker menu...")


def main():
    while True:
        display_main_menu()
        user_choice = get_main_menu_choice()

        if user_choice == '1':
            print("\n--- Entering Morning Activities ---")
            print("this morning you will do a free write, ")
            free_write_activity()
            pass
        elif user_choice == '2':
            print("\n--- Entering Evening Reflections ---")
            # evening reflections
            pass
        elif user_choice == '3':
             emotion_tracker_activity()  # enter the emotion tracker activity

        elif user_choice == '4':
            print("\n--- Viewing Past Entries and Emotions ---")
            # viewing past entries
            pass
        elif user_choice == '5':
            print("\n--- Jumping To A Specific Activity ---")
            # jump to a specific activity here
            pass
        elif user_choice == '6':
            print("Exiting the Wellness Journal. Take care of yourself!")
            break

if __name__ == "__main__":
    main()