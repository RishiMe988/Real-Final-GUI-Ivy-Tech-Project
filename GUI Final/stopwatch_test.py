import tkinter as tk
from tkinter import messagebox, ttk
import time
from datetime import datetime

# Define color constants from the palette
BG_COLOR = "#C1AE9F"
BUTTON_COLOR = "#69385C"
TEXT_COLOR = "white"

# Define a new window as a subclass of Toplevel
class StopwatchTestWindow(tk.Toplevel):
    def __init__(self, master):
        """
        Initialize the stopwatch window.

        Args:
        - master: The parent tkinter window.
        """
        super().__init__(master)
        self.title("Stopwatch Timing Test")
        self.geometry("400x300")
        self.configure(bg=BG_COLOR)  # Set background color

        # Initialize variables to manage stopwatch state
        self.running = False
        self.start_time = None

        # Stopwatch label
        self.stopwatch_label = tk.Label(self, text="00:00:00", bg=BG_COLOR, fg=TEXT_COLOR)
        self.stopwatch_label.pack(pady=10)

        # Input box for text
        self.text_box = tk.Text(self, height=10, width=50)
        self.text_box.pack(pady=10)

        # Start button
        self.start_button = tk.Button(self, text="Start", command=self.start_stopwatch, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.start_button.pack()

        # Stop button (initially disabled until start)
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED, bg=BUTTON_COLOR,
                                     fg=TEXT_COLOR)
        self.stop_button.pack()

        # Go back button (closes the stopwatch window)
        self.go_back_button = tk.Button(self, text="Go Back", command=self.destroy, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.go_back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def start_stopwatch(self):
        """
        Start the stopwatch and update UI accordingly.
        """
        self.running = True
        self.start_time = time.time()  # Record the starting time
        self.update_stopwatch()  # Begin updating the stopwatch display

        # Disable the start button and enable the stop button
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_stopwatch(self):
        """
        Stop the stopwatch, calculate results, and display them.
        """
        self.running = False
        elapsed_time = time.time() - self.start_time  # Calculate elapsed time

        # Calculate number of words and characters from the text input
        text_content = self.text_box.get("1.0", tk.END)
        words = len(text_content.split())
        characters = len(text_content.replace(" ", "").replace("\n", ""))

        # Calculate characters per second
        if elapsed_time > 0:
            chars_per_second = characters / elapsed_time
        else:
            chars_per_second = 0

        # Format elapsed time into hours, minutes, seconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        # Prepare result text to display in a message box
        result_text = f"Time: {hours:02}:{minutes:02}:{seconds:02}\n"
        result_text += f"Words: {words}\n"
        result_text += f"Characters: {characters}\n"
        result_text += f"Characters per second: {chars_per_second:.2f}\n"

        # Show results in a message box
        messagebox.showinfo("Results", result_text)

        # Update the stopwatch label with the final time display
        self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        # Enable the start button and disable the stop button
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_stopwatch(self):
        """
        Update the stopwatch display every second while running.
        """
        if self.running:
            elapsed_time = time.time() - self.start_time  # Calculate elapsed time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")  # Update display
            self.after(1000, self.update_stopwatch)  # Schedule the next update after 1 second

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")

    def open_stopwatch_window():
        """
        Function to open the stopwatch window.
        """
        stopwatch_window = StopwatchTestWindow(root)

    # Button to open the stopwatch window
    start_stopwatch_button = tk.Button(root, text="Open Stopwatch", command=open_stopwatch_window, bg=BUTTON_COLOR,
                                       fg=TEXT_COLOR)
    start_stopwatch_button.pack(pady=50)  # Place button in the main window

    root.mainloop()  # Start the tkinter main event loop


"""Imports and Constants:

Imported necessary modules (tkinter, time, datetime, messagebox).
Defined color constants for the UI.
StopwatchTestWindow Class:

Initialization (__init__): Sets up the stopwatch window with labels, buttons, and text input. Initializes variables for stopwatch state.

start_stopwatch Method: Starts the stopwatch, records start time, updates UI by disabling/enabling buttons.

stop_stopwatch Method: Stops the stopwatch, calculates elapsed time, counts words and characters from the input, computes characters per second, formats results, displays them in a message box, updates the stopwatch label, and adjusts button states.

update_stopwatch Method: Updates the stopwatch display every second while running using after() method for recursive scheduling.

Main Application (__main__):

open_stopwatch_window Function: Opens the stopwatch window when called.

Button Creation: Creates a button in the main window (root) that triggers open_stopwatch_window function when clicked.

Main Event Loop (root.mainloop()): Starts the main tkinter event loop to handle user inputs and window operations."""