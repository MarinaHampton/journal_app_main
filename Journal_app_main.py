# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 04/30/2025
# Description:
# - Sprint 1 main program
# main menu
# get user choice

from datetime import datetime
from ASCII_art import logo_2

def display_main_menu():
    print("-----------| Wellness Journal |---------- ")
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
    print("3. View Past Entries and Emotions")
    print("   - view your personal journey over time, identify emotional patterns and gain")
    print("     valuable self-awareness")
    print()
    print("4. Jump To A Specific Activity")
    print("   - quickly access any of the journaling features")
    print()
    print("5. Exit")
    print("-" * 45)

def get_user_choice():
    while True:
        choice = input("Enter your choice (1-5):> ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    while True:
        display_main_menu()
        user_choice = get_user_choice()

        if user_choice == '1':
            print("\n--- Entering Morning Activities ---")
            # =morning activities
            pass
        elif user_choice == '2':
            print("\n--- Entering Evening Reflections ---")
            # evening reflections
            pass
        elif user_choice == '3':
            print("\n--- Viewing Past Entries and Emotions ---")
            # viewing past entries here
            pass
        elif user_choice == '4':
            print("\n--- Jumping To A Specific Activity ---")
            # jump to a specific activity here
            pass
        elif user_choice == '5':
            print("Exiting the Wellness Journal App. Take care!")
            break

if __name__ == "__main__":
    main()