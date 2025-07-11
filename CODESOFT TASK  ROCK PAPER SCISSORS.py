import tkinter as tk
import random

# --- Main Logic Function ---
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You Win!"
    else:
        result = "💻 Computer Wins!"

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

# --- Main Window ---
root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Task 4")
root.geometry("400x300")
root.configure(bg="lightblue")

# --- Title Label ---
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=10)

# --- Result Display ---
result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue", justify="center")
result_label.pack(pady=20)

# --- Buttons ---
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Arial", 14), width=10,
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=10)

# --- Run the App ---
root.mainloop()
