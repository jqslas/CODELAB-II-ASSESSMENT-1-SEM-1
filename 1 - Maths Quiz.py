import random
import tkinter as tk
from tkinter import messagebox

# Create the main window and set its title and size
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("380x260")

# Variables to track the quiz state
level = ""      # Selected difficulty ("Easy", "Moderate", or "Advanced")
q_count = 0     # Number of questions shown so far (up to 10)
score = 0       # User's total score out of 100
tries = 1       # Current attempt for the active question (1 or 2)
a = 0           # First number in the problem
b = 0           # Second number in the problem
op = "+"        # Math operator ("+" or "-")
ans = 0         # Correct answer to the current problem


def clear():
    # Remove all widgets currently inside the window before drawing a new screen
    for w in root.winfo_children():
        w.destroy()


def randomInt(min_num, max_num):
    # Return a random whole number between min_num and max_num (inclusive)
    return random.randint(min_num, max_num)


def decideOperation():
    # Randomly pick "+" half the time and "-" half the time
    if random.randint(0, 1) == 0:
        return "+"
    return "-"


def new_question():
    global q_count, tries, a, b, op, ans

    # End the quiz and show results once 10 questions have been asked
    if q_count == 10:
        displayResults(score)
        return

    # Move to the next question and reset attempts back to 1
    q_count += 1
    tries = 1

    # Pick numbers based on the chosen difficulty level
    if level == "Easy":
        a = randomInt(1, 9)         # 1-digit numbers
        b = randomInt(1, 9)
    elif level == "Moderate":
        a = randomInt(10, 99)       # 2-digit numbers
        b = randomInt(10, 99)
    else:
        a = randomInt(1000, 9999)   # 4-digit numbers
        b = randomInt(1000, 9999)

    # Choose the operation and calculate the right answer
    op = decideOperation()
    if op == "+":
        ans = a + b
    else:
        ans = a - b

    # Show the new problem on screen
    displayProblem(a, b, op)


def isCorrect(user_ans, right_ans):
    global score, tries

    # Check if the user's answer matches the correct answer
    if user_ans == right_ans:
        # Award 10 points on first try, or 5 points on second try
        if tries == 1:
            score += 10
            messagebox.showinfo("Correct!", "Well done! +10 points")
        else:
            score += 5
            messagebox.showinfo("Correct!", "Good job! +5 points")
        new_question()
        return True

    # If wrong on the first try, give one more chance on the same question
    if tries == 1:
        tries = 2
        msg_label.config(text="Try again! One chance left (5 pts)")
        entry.delete(0, tk.END)
    else:
        # After two wrong tries, show the right answer and move on
        messagebox.showwarning("Wrong", f"Incorrect! The answer was {right_ans}")
        new_question()
    return False


def check_entry():
    # Convert the text from the input box into an integer
    try:
        user_ans = int(entry.get())
    except ValueError:
        # Handle non-number or blank input without crashing
        msg_label.config(text="Enter a whole number!")
        return
    isCorrect(user_ans, ans)


def displayProblem(num1, num2, sign):
    global entry, msg_label
    clear()

    # Show current question number and score at the top
    tk.Label(root, text=f"Question {q_count}/10   Score: {score}").pack(pady=8)
    # Show the math problem (e.g., 45 + 9 =)
    tk.Label(root, text=f"{num1} {sign} {num2} =", font=("Arial", 20)).pack(pady=10)

    # Text box for typing the answer, focused automatically
    entry = tk.Entry(root, width=10)
    entry.pack(pady=5)
    entry.focus()

    # Button to submit the answer and label for feedback/attempts
    tk.Button(root, text="Submit", command=check_entry).pack(pady=8)
    msg_label = tk.Label(root, text="Attempt 1 of 2")
    msg_label.pack()


def displayResults(final_score):
    clear()

    # Assign a grade/rank based on the final score out of 100
    if final_score > 90:
        grade = "A+"
    elif final_score >= 80:
        grade = "A"
    elif final_score >= 70:
        grade = "B"
    elif final_score >= 60:
        grade = "C"
    else:
        grade = "D / F"

    # Display final score and grade
    tk.Label(root, text="Quiz Over!", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text=f"Score: {final_score} / 100").pack(pady=4)
    tk.Label(root, text=f"Grade: {grade}").pack(pady=4)

    # Ask if the user wants to replay; show buttons if they say no
    again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if again:
        displayMenu()
    else:
        tk.Button(root, text="Play Again", command=displayMenu).pack(pady=6)
        tk.Button(root, text="Exit", command=root.destroy).pack()


def start_level(choice):
    global level, q_count, score
    # Reset quiz counters and start with the chosen difficulty
    level = choice
    q_count = 0
    score = 0
    new_question()


def displayMenu():
    clear()

    # Show difficulty menu options
    tk.Label(root, text="DIFFICULTY LEVEL", font=("Arial", 14)).pack(pady=12)
    tk.Button(root, text="1. Easy", width=18, command=lambda: start_level("Easy")).pack(pady=4)
    tk.Button(root, text="2. Moderate", width=18, command=lambda: start_level("Moderate")).pack(pady=4)
    tk.Button(root, text="3. Advanced", width=18, command=lambda: start_level("Advanced")).pack(pady=4)


# Launch the menu first and run the Tkinter event loop
displayMenu()
root.mainloop()