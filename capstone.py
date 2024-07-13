import tkinter as tk
from tkinter import messagebox


def count_words():
    text = entry.get("1.0", tk.END).strip()  # Get text from the Text widget
    words = text.split()  # Split text into words
    word_counts = {}  # Dictionary to store word counts

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    total_words = sum(word_counts.values())  # Calculate total number of words

    # Display results in a message box
    result_message = f"Total number of words: {total_words}\n\nWord Counts:\n"
    for word, count in word_counts.items():
        result_message += f"{word}: {count}\n"

    messagebox.showinfo("Word Count Results", result_message.strip())


def quit_app():
    root.quit()  # Quit the main loop and close the application


# Create main application window
root = tk.Tk()
root.title("Word Counter")

# Create Text widget for user input
entry = tk.Text(root, height=10, width=50, wrap=tk.WORD)
entry.pack(pady=10)

# Create button to trigger word counting
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack(side=tk.LEFT, padx=10)

# Create quit button
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(side=tk.RIGHT, padx=10)

# Run the main event loop
root.mainloop()
