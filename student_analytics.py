# ==============================================================================
# STUDENT PERFORMANCE ANALYTICS DASHBOARD
# Practicing: Lists, Tuples, Dictionaries, If-Else, Functions, For/While Loops
# ==============================================================================

def calculate_stats(scores):
    """
    Calculates student average, assigns a grade, and determines pass/fail status.
    Demonstrates: List iteration, math operations, conditionals, tuple returns.
    """
    if not scores:
        return (0.0, "N/A", "No Scores")

    # Summing score elements using a for loop
    total = 0
    for score in scores:
        total += score

    average = total / len(scores)

    # Grading logic using if-elif-else statements
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if average >= 60 else "Fail"

    # Returning immutable summary package as a Tuple
    return (round(average, 2), grade, status)


def add_student_record(database):
    """
    Collects student name and scores, adding them to the primary dictionary.
    Demonstrates: Input handling, list population, dictionary mutation, input validation with while loops.
    """
    print("\n--- ADD / UPDATE STUDENT RECORD ---")
    name = input("Enter student name: ").strip().title()

    if name in database:
        print(f"Notice: '{name}' already exists. Inputting new scores will overwrite existing record.")

    scores = []  # List to store scores
    num_exams = 3

    print(f"Enter {num_exams} exam scores for {name}:")
    for i in range(1, num_exams + 1):
        # Validation loop to handle non-numeric inputs gracefully
        while True:
            try:
                score = float(input(f"  Score for Exam {i} (0-100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("  Invalid range! Score must be between 0 and 100.")
            except ValueError:
                print("  Invalid entry! Please enter a valid number.")

    # Dictionary update: Key = Student Name, Value = List of Scores
    database[name] = scores
    print(f" Successfully saved record for {name}.")


def display_all_students(database):
    """
    Iterates through the dictionary and outputs formatted analytics.
    Demonstrates: Dictionary iteration (.items()), tuple unpacking.
    """
    print("\n--- CLASS PERFORMANCE REPORT ---")
    if not database:
        print("No student records found in the database.")
        return

    print(f"{'Name':<12} | {'Scores':<20} | {'Average':<8} | {'Grade':<6} | {'Status':<6}")
    print("-" * 65)

    # Iterating over key-value pairs in dictionary
    for name, scores in database.items():
        # Unpacking the tuple returned by calculate_stats
        avg, grade, status = calculate_stats(scores)
        print(f"{name:<12} | {str(scores):<20} | {avg:<8} | {grade:<6} | {status:<6}")


def find_top_performer(database):
    """
    Evaluates all students to find the highest average score.
    Demonstrates: Variable tracking inside search loops.
    """
    print("\n--- TOP PERFORMER ANALYSIS ---")
    if not database:
        print("No student records available.")
        return

    top_student = None
    highest_avg = -1.0

    for name, scores in database.items():
        avg, _, _ = calculate_stats(scores)
        if avg > highest_avg:
            highest_avg = avg
            top_student = name

    if top_student:
        print(f" Top Performer: {top_student} with an average score of {highest_avg}")


def filter_by_threshold(database):
    """
    Filters students whose average score meets or exceeds a target threshold.
    Demonstrates: Filtering condition inside loop, collecting matching results.
    """
    print("\n--- FILTER BY TARGET AVERAGE ---")
    if not database:
        print("No student records available.")
        return

    try:
        threshold = float(input("Enter minimum average score threshold (e.g., 75): "))
    except ValueError:
        print("Invalid entry! Must be a numeric value.")
        return

    matching_students = []

    for name, scores in database.items():
        avg, grade, status = calculate_stats(scores)
        if avg >= threshold:
            matching_students.append((name, avg, grade))  # Storing tuple in list

    if matching_students:
        print(f"\nStudents meeting or exceeding average of {threshold}:")
        for name, avg, grade in matching_students:
            print(f" - {name}: Avg = {avg} (Grade {grade})")
    else:
        print(f"No students achieved an average of {threshold} or higher.")


def main():
    """
    Main application control loop using a menu system.
    Demonstrates: Dictionary initialization, main program control loop.
    """
    # Pre-populated Dictionary data structure
    student_database = {
        "Alice": [88.5, 92.0, 95.0],
        "Bob": [65.0, 70.5, 68.0],
        "Charlie": [78.0, 82.5, 80.0]
    }

    # Interactive application loop
    running = True
    while running:
        print("\n=================================")
        print("  STUDENT ANALYTICS DASHBOARD")
        print("=================================")
        print("1. Add or Update Student Record")
        print("2. View All Student Reports")
        print("3. Find Top Performer")
        print("4. Filter Students by Score Threshold")
        print("5. Exit Application")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            add_student_record(student_database)
        elif choice == "2":
            display_all_students(student_database)
            input("\nPress Enter to return to the menu...")  # Keeps output on screen until you hit Enter

        elif choice == "3":
            find_top_performer(student_database)
            input("\nPress Enter to return to the menu...")

        elif choice == "4":
            filter_by_threshold(student_database)
            input("\nPress Enter to return to the menu...")
        elif choice == "5":
            print("\nExiting application. Best of luck on your MSc in Data Science journey!")
            running = False
        else:
            print("Invalid menu selection. Please choose a number from 1 to 5.")


# Standard entry point execution
if __name__ == "__main__":
    main()