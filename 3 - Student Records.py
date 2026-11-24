import tkinter as tk

root = tk.Tk()
root.title("Student Manager")
root.geometry("500x430")

# Takes all lines that aren't empty from the txt file
with open("3.5 - students.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Break down each student row and calculate totals, percentage and grades
students = []
for line in lines[1:]:
    parts = line.split(",")
    code = parts[0]
    name = parts[1]
    cw = int(parts[2]) + int(parts[3]) + int(parts[4]) # Three quiz scores , each out of 20
    exam = int(parts[5])
    total = cw + exam # Out of 160 total (4 graded items that add up to 160 total)
    pct = (total / 160) * 100
    # Assign grade ranges / boundaries
    if pct >= 70:
        grade = "A"
    elif pct >= 60:
        grade = "B"
    elif pct >= 50:
        grade = "C"
    elif pct >= 40:
        grade = "D"
    else:
        grade = "F"

    students.append((code, name, cw, exam, total, pct, grade))


def show_text(msg):
    # Removes old text and writes the new output in the textbox
    box.delete("1.0", tk.END)
    box.insert(tk.END, msg)


def format_one(s):
    # Unpack tuple and assign variables to each students breakdown
    code, name, cw, exam, total, pct, grade = s
    return (
        f"Name: {name}\n"
        f"Student Number: {code}\n"
        f"Coursework Total: {cw} / 60\n"
        f"Exam Mark: {exam} / 100\n"
        f"Overall Percentage: {pct:.1f}%\n"
        f"Grade: {grade}\n"
    )


def view_all():
    # Shows every students record, class count and average percentage
    text = ""
    total_pct = 0
    for s in students:
        text += format_one(s) + "--------------------------\n"
        total_pct += s[5]
    avg = total_pct / len(students)
    text += f"\nStudents in class: {len(students)}\n"
    text += f"Average Percentage: {avg:.1f}%"
    show_text(text)


def view_one():
    # Check what the user clicked in the listbox
    sel = listbox.curselection()
    if not sel:
        show_text("Click a student in the list first.")
        return
    show_text(format_one(students[sel[0]]))


def highest():
    # Checks the students with the highest score
    best = students[0]
    for s in students:
        if s[4] > best[4]:
            best = s
    show_text("Highest Score:\n--------------------------\n" + format_one(best))


def lowest():
    # Checks the list for the student with the lowest score
    worst = students[0]
    for s in students:
        if s[4] < worst[4]:
            worst = s
    show_text("Lowest Score:\n--------------------------\n" + format_one(worst))


# Main menu buttons
tk.Button(root, text="1. View All Student Records", command=view_all).pack(pady=3)
tk.Button(root, text="2. View Individual Student Record", command=view_one).pack(pady=3)
tk.Button(root, text="3. Highest Total Score", command=highest).pack(pady=3)
tk.Button(root, text="4. Lowest Total Score", command=lowest).pack(pady=3)

# Listbox that stores all the students so user can pick one for option 2
listbox = tk.Listbox(root, height=4, width=35)
for s in students:
    listbox.insert(tk.END, f"{s[0]} - {s[1]}")
listbox.pack(pady=4)

# Main textbox display for all the outputs
box = tk.Text(root, width=56, height=13)
box.pack(pady=5)

root.mainloop()