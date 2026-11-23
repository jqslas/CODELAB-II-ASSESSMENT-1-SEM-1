import random
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Alexa Jokes")
root.geometry("400x260")

# Store current punchline
punchline = ""

# Read all non-empty lines from randomJokes.txt
with open("2.5 - alexajokes.txt", "r", encoding="utf-8") as f:
    jokes = [line.strip() for line in f if line.strip()]


def get_joke():
    global punchline
    # Pick a random line and split at "?" into setup and punchline
    joke = random.choice(jokes)
    q, p = joke.split("?", 1)

    # Show setup and hide old punchline
    setup_lbl.config(text=q + "?")
    punch_lbl.config(text="")
    punchline = p.strip()


def show_punch():
    # Show the punchline below the setup
    punch_lbl.config(text=punchline)


# Buttons and labels
tk.Button(root, text="Alexa tell me a Joke", command=get_joke).pack(pady=10)

setup_lbl = tk.Label(root, text="", wraplength=360)
setup_lbl.pack(pady=8)

punch_lbl = tk.Label(root, text="", wraplength=360)
punch_lbl.pack(pady=8)

tk.Button(root, text="Show Punchline", command=show_punch).pack(pady=4)
tk.Button(root, text="Next Joke", command=get_joke).pack(pady=4)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=4)

root.mainloop()