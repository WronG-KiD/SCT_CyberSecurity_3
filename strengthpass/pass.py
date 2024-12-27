import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def assess_password_strength(password):
   
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'\d', password)),
        "special_characters": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }
    
    strength_score = sum(criteria.values())
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak",
    }
    
    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not criteria["numbers"]:
        feedback.append("Password should contain at least one numeric digit.")
    if not criteria["special_characters"]:
        feedback.append("Password should contain at least one special character (!@#$%^&*(), etc.).")
    
    return strength_levels[strength_score], feedback

def check_password():
    """
    Callback function for assessing password strength.
    """
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    
    strength, feedback = assess_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", foreground=color_mapping[strength])
    
    # Display detailed feedback
    feedback_text.delete(1.0, tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions to improve:\n")
        for suggestion in feedback:
            feedback_text.insert(tk.END, f"- {suggestion}\n")
    else:
        feedback_text.insert(tk.END, "Your password is very strong!")

# Color mapping for strength levels
color_mapping = {
    "Very Strong": "green",
    "Strong": "blue",
    "Moderate": "orange",
    "Weak": "red",
    "Very Weak": "dark red"
}

# Create GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.configure(bg="#f7f7f7")

# Apply styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12), background="#f7f7f7")
style.configure("TEntry", font=("Helvetica", 12))

# Header Label
header_label = ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

# Input Label and Entry
password_label = ttk.Label(root, text="Enter your password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(root, show="*", width=40)
password_entry.pack(pady=5)

# Check Password Button
check_button = ttk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=15)

# Result Label
result_label = ttk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=5)

# Feedback Text Area
feedback_frame = tk.Frame(root, bg="#f7f7f7", bd=2, relief="groove")
feedback_frame.pack(pady=10, fill="both", expand=True)
feedback_text = tk.Text(feedback_frame, width=50, height=10, wrap="word", state="normal", font=("Helvetica", 12))
feedback_text.pack(pady=5, padx=5)

# Run the GUI Application
root.mainloop()
