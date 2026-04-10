import tkinter as tk
from tkinter import scrolledtext
import random

# --- The Markov Logic ---
def build_model(text):
    words = text.split()
    model = {}
    for i in range(len(words) - 1):
        if words[i] not in model:
            model[words[i]] = []
        model[words[i]].append(words[i+1])
    return model

def generate_markov_text():
    # Get data from the UI boxes
    input_text = text_input.get("1.0", tk.END).strip()
    start_word = start_entry.get().strip()
    try:
        num_words = int(length_entry.get())
    except:
        num_words = 10

    if not input_text or not start_word:
        result_display.delete("1.0", tk.END)
        result_display.insert(tk.END, "Error: Please enter text and a start word.")
        return

    # Build and Generate
    model = build_model(input_text)
    
    if start_word not in model:
        result_display.delete("1.0", tk.END)
        result_display.insert(tk.END, f"Error: '{start_word}' not found in training text.")
        return

    current_word = start_word
    output = [current_word]
    
    for _ in range(num_words - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            output.append(next_word)
            current_word = next_word
        else:
            break
            
    # Display the result in the bottom box
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, " ".join(output))

# --- Setting up the Window ---
root = tk.Tk()
root.title("Markov Chain Text Generator")
root.geometry("600x650")

# 1. Training Text Section
tk.Label(root, text="Enter Training Text:", font=("Arial", 12, "bold")).pack(pady=5)
text_input = scrolledtext.ScrolledText(root, width=70, height=10)
text_input.pack(pady=5)

# 2. Settings Section
tk.Label(root, text="Start Word:").pack()
start_entry = tk.Entry(root, width=30)
start_entry.pack(pady=5)

tk.Label(root, text="Number of Words:").pack()
length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "20") # Default value
length_entry.pack(pady=5)

# 3. Generate Button
gen_button = tk.Button(root, text="Generate Text", command=generate_markov_text, 
                       bg="blue", fg="white", font=("Arial", 10, "bold"))
gen_button.pack(pady=20)

# 4. Results Section
tk.Label(root, text="Generated Text:", font=("Arial", 12, "bold")).pack(pady=5)
result_display = scrolledtext.ScrolledText(root, width=70, height=10, bg="#f0f0f0")
result_display.pack(pady=5)

root.mainloop()
