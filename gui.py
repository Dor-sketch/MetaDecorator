"""
This file contains the GUI for the Meta Class Modifier.
It uses tkinter to create the GUI.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os  # used to get the current directory
import tkinter as tk
from tkinter import ttk  # Import the ttk module
import sys
import random
import string

from meta import (
    read_file_content,
    restore_file_content,
    import_meta_class,
)

META = "mata"

EXAMPLE_CODE_USAGES = {
    "Performance Monitoring": """print(f'{original_function.__name__} took {round(get_time() - before, 3)} seconds')""",
    "Logging": """print(f"Calling {original_function.__name__} from {self.__class__.__name__} class")""",
    "Error Handling": """try:\n    original_function(*args, **kwargs)\nexcept Exception as e:\n    print(f"Error: {e}")""",
    "Custom Code": """self.name = 'Meta' + self.name\nprint(f'Hello, {self.name}')""",
    "Custom Code 2": """print(f'{self.name} account: {self.amt} dollars')""",
}


class FallingChar:
    def __init__(self, canvas, x, y, char=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.char = char if char else random.choice(string.ascii_letters)
        self.text_id = canvas.create_text(
            x, y, text=self.char, fill="green")  # Change color to green

    def fall(self, speed):
        self.y += speed
        self.canvas.move(self.text_id, 0, speed)


class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

    def flush(self):
        pass


class GUI:
    """
    A class to create the GUI for the Meta Class Modifier.
    """

    def __init__(self, master):
        self.master = master
        master.title("Meta Decorator")

        # Set the window size
        master.geometry("923x600")

        # Load the background image
        # Create a canvas for the falling characters
        self.canvas = tk.Canvas(master, bg='black')
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        with open('GUI.py', 'r') as f:
            chars = list(f.read().strip())

        # Create falling characters
        self.falling_chars = [FallingChar(self.canvas, random.randint(
            0, 800), random.randint(0, 600), char=random.choice(chars)) for _ in range(100)]
        # Create falling characters

        self.create_header()
        self.create_widgets()

    def update_falling_chars(self):
        for char in self.falling_chars:
            char.fall(random.randint(1, 10))  # Increase speed
            if char.y > 600:
                self.canvas.delete(char.text_id)
                char.y = 0
                char.text_id = self.canvas.create_text(
                    char.x, char.y, text=char.char, fill="green")
        self.master.after(100, self.update_falling_chars)

    def create_header(self):
        """
        Create the header of the GUI.
        """
        self.title = tk.Label(
            self.master, text="Meta Class Modifier", font=("Arial", 24, "bold"))
        self.title.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

    def clear_entry(self, event):
        """
        Clear the entry widget when it receives focus.
        """
        event.widget.delete(0, tk.END)
    def create_widgets(self):
        """
        Create the widgets of the GUI.
        """
        self.master.configure(bg='white')  # Set the background color to white

        tk.Label(self.master, text="File name:", font=("Courier", 24), fg="black", bg="white").grid(
            row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.file_entry = tk.Entry(self.master, font=("Courier", 24), fg="black", bg="white", insertbackground='black', width=20)
        self.file_entry.insert(0, "bank.py")  # Insert the default text
        self.file_entry.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.file_entry_title = tk.Label(self.master, text="Enter code to add or choose from presets:", font=("Courier", 24), fg="black", bg="white")
        self.file_entry_title.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.code_entry = tk.Text(self.master, font=("Courier", 24), fg="black", bg="white", insertbackground='black', width=20, height=3, wrap=tk.WORD)
        self.code_entry.grid(row=2, column=0, columnspan=6, sticky=tk.N+tk.S+tk.E+tk.W)
        self.modes = list(EXAMPLE_CODE_USAGES.keys())  # Get the modes from EXAMPLE_CODE_USAGES
        self.mode_var = tk.StringVar()
        self.mode_combobox = ttk.Combobox(self.master, textvariable=self.mode_var, values=self.modes, font=("Courier", 24))
        self.mode_combobox.current(0)  # Set the default mode to the first one
        self.mode_combobox.bind('<<ComboboxSelected>>', self.on_mode_selected)  # Bind the function to the combobox
        self.mode_combobox.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        tk.Button(self.master, text="Run", font=("Courier", 24), fg="black", bg="white", command=self.run).grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        tk.Button(self.master, text="Close", font=("Courier", 24), fg="black", bg="white", command=self.master.quit).grid(
            row=4, column=1, sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.output_text = tk.Text(self.master, font=("Courier", 24), fg="black", bg="white", insertbackground='black', width=20, height=3, wrap=tk.WORD)
        self.output_text.grid(row=5, column=0, columnspan=6, sticky=tk.N+tk.S+tk.E+tk.W)
        self.file_entry.bind("<Key>", self.adjust_width)

    def adjust_width(self, event):
        # Get the current content of the Text widget
        content = self.code_entry.get('1.0', 'end-1c')

        # Calculate the new width (the length of the content plus some padding)
        # Consider the width of the first line only
        new_width = len(content.split('\n')[0]) + 10

        # Set the new width
        self.code_entry.config(width=new_width)

    def browse(self):
        """
        Browse for a file.
        """
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("python files", "*.py"), ("all files", "*.*")),
        )
        self.file_entry.delete(0, "end")
        self.file_entry.insert(0, filename)

    def run(self):
        """
        Run the meta class modifier.
        """
        sys.stdout = TextRedirector(self.output_text)
        sys.stderr = TextRedirector(self.output_text)
        self.update_falling_chars()

        try:
            original_content = read_file_content(self.file_entry.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        try:
            import_meta_class(self.file_entry.get(),
                              self.code_entry.get('1.0', 'end-1c'))
            with open(self.file_entry.get(), "r", encoding="utf-8") as file:
                exec(file.read())
            restore_file_content(self.file_entry.get(), original_content)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            restore_file_content(self.file_entry.get(), original_content)

    def on_mode_selected(self, event):
        # Get the selected mode
        selected_mode = self.mode_combobox.get()

        # Look up the code for the selected mode
        code = EXAMPLE_CODE_USAGES.get(selected_mode)

        # Insert the code into the text entry widget
        if code:
            # Clear the text entry widget
            self.code_entry.delete('1.0', tk.END)
            self.code_entry.insert('1.0', code)  # Insert the code
