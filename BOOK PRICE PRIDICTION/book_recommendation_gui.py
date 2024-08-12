import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the book data
books = pd.read_csv(r'E:\download\elevate\book price\books.csv')

def get_books_by_mood(mood):
    # Filter books based on the selected mood
    filtered_books = books[books['mood'].str.contains(mood, case=False, na=False)]
    return filtered_books[['title', 'author', 'description']]

def show_recommendations():
    mood = mood_combobox.get()
    if not mood:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select a mood.")
        return
    
    recommendations = get_books_by_mood(mood)
    result_text.delete(1.0, tk.END)  # Clear previous results
    if recommendations.empty:
        result_text.insert(tk.END, "No recommendations available for this mood.")
    else:
        for index, row in recommendations.iterrows():
            result_text.insert(tk.END, f"Title: {row['title']}\nAuthor: {row['author']}\nDescription: {row['description']}\n\n")

# Create the main application window
root = tk.Tk()
root.title("Book Recommendation System")

# Set window size and position
root.geometry("600x400")
root.resizable(False, False)

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="Book Recommendation System", font=("Arial", 18, "bold"))
title_label.pack(pady=(0, 20))

instruction_label = tk.Label(frame, text="Select a mood to get book recommendations:", font=("Arial", 12))
instruction_label.pack(pady=(0, 10))

mood_combobox = ttk.Combobox(frame, values=["Serious", "Dark", "Romantic", "Melancholic", "Adventurous", "Inspirational"], font=("Arial", 12))
mood_combobox.pack(pady=(0, 20))
mood_combobox.set("Select Mood")

get_recommendations_button = tk.Button(frame, text="Get Recommendations", command=show_recommendations, font=("Arial", 12, "bold"))
get_recommendations_button.pack(pady=(0, 20))

result_text = tk.Text(frame, height=15, width=70, wrap=tk.WORD, font=("Arial", 10))
result_text.pack(pady=(0, 20))
result_text.config(state=tk.DISABLED)  # Disable editing

# Start the GUI event loop
root.mainloop()
