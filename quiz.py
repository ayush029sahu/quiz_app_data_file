import json
import random

users = {}


def load_quiz_data():
    """Load quiz data from a file."""
    try:
        with open("quiz_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Quiz data file not found!")
        return {}

def save_quiz_data(data):
    """Save quiz data to a file."""
    with open("quiz_data.json", "w") as file:
        json.dump(data, file, indent=4)

def register():
    name = input("Enter a username: ")
    if name in users:
        print("User already exists!")
        return False
    pwd = input("Enter a password: ")
    users[name] = pwd
    print("Registration successful!")
    return True

def login():
    name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if users.get(name) == pwd:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

def quiz(subject, user, quiz_data):
    print(f"\nStarting {subject} quiz!")
    score = 0
    questions = random.sample(quiz_data[subject], len(quiz_data[subject]))

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q['o'], 1):
            print(f"{idx}. {option}")
        try:
            ans = int(input("Your answer (1/2/3/4): "))
            if q['o'][ans - 1] == q['a']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['a']}")
        except (ValueError, IndexError):
            print("Invalid input! Skipping this question.")

    print(f"\n{user}, your score is {score}/5.")

def main():
    print("Welcome to the Quiz Application!")
     # Load quiz data
    global quiz_data
    quiz_data = load_quiz_data()

    if not quiz_data:
        print("No quiz data available. Exiting the application.")
        return
    user = None

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            user = login()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    # Initialize attempts and subjects_taken
    attempts = 0
    subjects_taken = set()

    # Main loop to allow exactly 3 quizzes
    while attempts < 3:
        print("\nSubjects:\n1. DBMS\n2. Python\n3. DSA")
        choice = input("Choose a subject (1-3): ").strip()

        if choice == "1" and "DBMS" not in subjects_taken:
            quiz("DBMS", user, quiz_data)
            subjects_taken.add("DBMS")
            attempts += 1
        elif choice == "2" and "Python" not in subjects_taken:
            quiz("Python", user, quiz_data)
            subjects_taken.add("Python")
            attempts += 1
        elif choice == "3" and "DSA" not in subjects_taken:
            quiz("DSA", user, quiz_data)
            subjects_taken.add("DSA")
            attempts += 1
        else:
            if choice in ["1", "2", "3"]:
                print("You have already taken this quiz. Please choose a different subject.")
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    print("You have completed all 3 quizzes. Goodbye!")

if __name__ == "__main__":
    main()

