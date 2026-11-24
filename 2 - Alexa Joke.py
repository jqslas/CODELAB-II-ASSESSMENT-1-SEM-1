import random
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Alexa Jokes")
root.geometry("400x260")

font = ("Segoe UI", 10)
buttonbg = "lightblue"

# Holds the punchline until the user reveals it
punchline = ""

# Read all the non-empty lines from 2.5 - alexajokes.txt
with open("2.5 - alexajokes.txt", "r", encoding="utf-8") as f:
    jokes = [line.strip() for line in f if line.strip()]


def takejokefile():
    global punchline
    # Pick a random line and split it where the ? is
    joke = random.choice(jokes)
    # Assign the split joke and punchline to a variable
    q, p = joke.split("?", 1)

    # Show setup with a ? and clears the previous punchline
    setup1.config(text=q + "?")
    punch1.config(text="")
    # Saves the cleaned punchline for when the user reveals it
    punchline = p.strip()


def punchlineshow():
    # Reveals the saved punchline 
    punch1.config(text=punchline)


# Button to fetch a new joke when clicked
tk.Button(root, text="Alexa tell me a Joke", command=takejokefile, bg=buttonbg, font=font).pack(pady=10)
# Labels for displaying the joke and punchline 
setup1 = tk.Label(root, text="", wraplength=360, bg=buttonbg, font=font)
setup1.pack(pady=8)

punch1 = tk.Label(root, text="", wraplength=360, bg=buttonbg, font=font)
punch1.pack(pady=8)
# Action buttons to show the punchline, move to the next joke or to exit the program
tk.Button(root, text="Show Punchline", command=punchlineshow, bg=buttonbg, font=font).pack(pady=4)
tk.Button(root, text="Next Joke", command=takejokefile, bg=buttonbg, font=font).pack(pady=4)
tk.Button(root, text="Quit", command=root.destroy, bg=buttonbg, font=font).pack(pady=4)
# Launch the program and wait for user to interact
root.mainloop()

