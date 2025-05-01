# Author: Marina Hampton
# GitHub username: MarinaHampton
# Date: 04/30/2025
# Description:
# includes "morning activities" for journal app
# free_write_activity

from datetime import datetime
import random


def get_writing_prompt():
    prompts = [
        "What are you grateful for today?",
        "Describe a small act of kindness you witnessed or performed.",
        "What is a goal you have for the week and why is it important to you?",
        "Write about a place where you feel completely at peace.",
        "What is a challenge you are currently facing and how are you approaching it?",
        "Describe a memory that makes you smile.",
        "What is something you want to learn or explore?",
        "Write about your current emotional state and why you think you feel this way.",
        "If you could have a conversation with anyone (living or deceased), who would it be and what would you talk about?",
        "What is a small step you can take today to improve your well-being?"
    ]
    return random.choice(prompts)

def free_write_activity():
    print("\n--- Morning Free Write ---")
    print(" Use the space below to express yourself.")
    print("Feeling uninspired? Enter PROMPT on a new line for a writing prompt")
    print("Type 'DONE' on a new line to save and exit.")

    print("-" * 40)

    lines = []
    while True:
        line = input("> ")
        if line.upper() == 'DONE':
            break
        elif line.upper() == 'PROMPT':
            prompt = get_writing_prompt()
            print(f"\nHere is a prompt for you: {prompt}\n")
        else:
            lines.append(line)

    if lines:
        entry_content = "\n".join(lines)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_journal_entry(timestamp, entry_content, "morning_free_write") # Still needs to be defined here or imported
        print(f"\nEntry saved at {timestamp}")
    else:
        print("\nNo entry written.")

    input("Press Enter to return to the main menu...")

def save_journal_entry(timestamp, content, activity_type):
    filename = "journal_entries.txt"  # Example filename
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] ({activity_type}):\n{content}\n\n")


