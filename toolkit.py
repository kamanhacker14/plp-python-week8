# Personal Mini-Toolkit
# A menu-driven program with four tools:
# 1. Number Guessing Game  2. To-Do List  3. Simple Calculator  4. Name Formatter

import random

# The to-do list is created BEFORE the menu loop so tasks are remembered
# every time the user comes back to the To-Do tool.
todo_list = []

print("Welcome to your Personal Mini-Toolkit!")

# ---------------------------------------------------------------
# MAIN MENU LOOP - runs until the user chooses Quit (option 5)
# ---------------------------------------------------------------
while True:
    print()
    print("==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Name Formatter")
    print("5. Quit")
    print("------------------------------")
    choice = input("Choose an option (1-5): ").strip()

    # -----------------------------------------------------------
    # TOOL 1: Number Guessing Game
    # The computer picks a secret number from 1 to 20. A loop keeps asking
    # for guesses and uses conditionals to say "too low", "too high" or
    # "correct" until the player wins or types q to give up.
    # -----------------------------------------------------------
    if choice == "1":
        secret = random.randint(1, 20)
        attempts = 0
        print()
        print("--- Number Guessing Game ---")
        print("I'm thinking of a number between 1 and 20.")

        while True:
            guess_text = input("Your guess (or 'q' to give up): ").strip().lower()

            if guess_text == "q":
                print(f"No problem! The secret number was {secret}.")
                break

            if not guess_text.isdigit():
                print("Please enter a whole number between 1 and 20.")
                continue

            guess = int(guess_text)
            attempts += 1

            if guess < secret:
                print(f"{guess} is too low. Try a higher number!")
            elif guess > secret:
                print(f"{guess} is too high. Try a lower number!")
            else:
                print(f"Correct! You found {secret} in {attempts} guesses. Well done!")
                break

    # -----------------------------------------------------------
    # TOOL 2: To-Do List
    # Uses a LIST (todo_list) that changes while the program runs:
    # tasks are added with append() and removed with pop().
    # A loop keeps the to-do sub-menu open until the user goes back.
    # -----------------------------------------------------------
    elif choice == "2":
        print()
        print("--- To-Do List ---")

        while True:
            print()
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")
            todo_choice = input("Choose an option (1-4): ").strip()

            if todo_choice == "1":
                task = input("Enter the new task: ").strip()
                if task == "":
                    print("A task can't be empty. Nothing was added.")
                else:
                    todo_list.append(task)
                    print(f"Added '{task}'. You now have {len(todo_list)} task(s).")

            elif todo_choice == "2":
                if len(todo_list) == 0:
                    print("Your to-do list is empty. Enjoy the free time!")
                else:
                    print("Your tasks:")
                    for number, task in enumerate(todo_list, start=1):
                        print(f"  {number}. {task}")

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("There is nothing to remove - your list is empty.")
                else:
                    print("Your tasks:")
                    for number, task in enumerate(todo_list, start=1):
                        print(f"  {number}. {task}")
                    remove_text = input("Number of the task to remove: ").strip()

                    if remove_text.isdigit() and 1 <= int(remove_text) <= len(todo_list):
                        removed = todo_list.pop(int(remove_text) - 1)
                        print(f"Removed '{removed}'. Great job getting things done!")
                    else:
                        print(f"'{remove_text}' is not a valid task number.")

            elif todo_choice == "4":
                print("Going back to the main menu...")
                break

            else:
                print(f"'{todo_choice}' is not an option. Please choose 1 to 4.")

    # -----------------------------------------------------------
    # TOOL 3: Simple Calculator
    # Asks for two numbers and an operation, then uses if / elif / else
    # to calculate. It checks for division by zero and uses try / except
    # so typing letters instead of numbers does not crash the program.
    # -----------------------------------------------------------
    elif choice == "3":
        print()
        print("--- Simple Calculator ---")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("That wasn't a valid number. Returning to the main menu.")
        else:
            operation = input("Choose an operation (+, -, *, /): ").strip()
            result = None

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Oops! You can't divide by zero.")
                else:
                    result = num1 / num2
            else:
                print(f"'{operation}' is not a valid operation. Use +, -, * or /.")

            if result is not None:
                print(f"{num1} {operation} {num2} = {result}")

    # -----------------------------------------------------------
    # TOOL 4: Name Formatter
    # Takes a name and shows it in neat capitalisation, in capital letters,
    # as initials (a loop goes through each word) and its length.
    # A conditional stops empty names.
    # -----------------------------------------------------------
    elif choice == "4":
        print()
        print("--- Name Formatter ---")
        name = input("Enter your full name: ").strip()

        if name == "":
            print("You didn't type a name. Please try again next time.")
        else:
            words = name.split()
            initials = ""
            for word in words:
                initials += word[0].upper() + "."

            print(f"Neat format : {name.title()}")
            print(f"Capitals    : {name.upper()}")
            print(f"Initials    : {initials}")
            print(f"Characters  : {len(name)}")
            print(f"Nice to meet you, {words[0].title()}!")

    # -----------------------------------------------------------
    # QUIT: leaves the main loop and ends the program
    # -----------------------------------------------------------
    elif choice == "5":
        print()
        print("Thanks for using the toolkit. Goodbye!")
        break

    # -----------------------------------------------------------
    # INVALID CHOICE: polite message, then the menu shows again
    # -----------------------------------------------------------
    else:
        print(f"Oops! '{choice}' is not on the menu. Please choose a number from 1 to 5.")
