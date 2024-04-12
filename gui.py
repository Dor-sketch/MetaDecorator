"""
This file contains the GUI for the Meta Class Modifier.
It uses tkinter to create the GUI.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os  # used to get the current directory
from PIL import Image, ImageTk  # Import from Pillow
import tkinter as tk
from tkinter import ttk  # Import the ttk module

from meta import (
    read_file_content,
    restore_file_content,
    import_meta_class,
)

EXAMPLE_CODE_USAGES = {
    "Performance Monitoring": """
from time import time
start = time()
yield  # original function executes here
end = time()
print(f"{original_function.__name__} took {end - start} seconds")
""",
"Logging": """
print(f"Calling {original_function.__name__}")
yield  # original function executes here
print(f"{original_function.__name__} finished")
"""
}


class GUI:
    """
    A class to create the GUI for the Meta Class Modifier.
    """
    def __init__(self, master):
        self.master = master
        master.title("Meta Class Modifier")

        # Load the background image
        self.background_image = Image.open("./images/backround.png")
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Set the background image
        self.background_label = tk.Label(master, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_header()
        self.create_widgets()

    def create_header(self):
        """
        Create the header of the GUI.
        """
        self.title = tk.Label(
            self.master, text="Meta Class Modifier", font=("Arial", 24, "bold"))
        self.title.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

    def create_widgets(self):
        """
        Create the widgets of the GUI.
        """
        tk.Label(self.master, text="Enter python file name:").grid(
            row=0, column=0)
        self.file_entry = tk.Entry(self.master, font=("Arial", 22), bg="black", fg="white", insertbackground="white", width=10)
        self.file_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Browse",
                  command=self.browse,).grid(row=0, column=2)

        tk.Label(self.master, text="Enter python code:").grid(row=1, column=0)

        # Existing code

        # Existing code
        # Existing code
        self.code_entry = tk.Entry(self.master, font=("Arial", 22), bg="black", fg="white", insertbackground="white", width=10)
        self.code_entry.bind('<KeyRelease>', self.adjust_width)  # Bind the function to the KeyRelease event
        self.code_entry.grid(row=1, column=1)

        # New code
        self.modes = list(EXAMPLE_CODE_USAGES.keys())  # Get the modes from EXAMPLE_CODE_USAGES
        self.mode_var = tk.StringVar()
        self.mode_combobox = ttk.Combobox(self.master, textvariable=self.mode_var, values=self.modes)
        self.mode_combobox.current(0)  # Set the default mode to the first one
        self.mode_combobox.bind('<<ComboboxSelected>>', self.on_mode_selected)  # Bind the function to the combobox
        self.mode_combobox.grid(row=1, column=2)
        self.mode_combobox.grid(row=1, column=2)  # Use grid instead of pack to place the combobox
        tk.Button(self.master, text="Run",
                  command=self.run).grid(row=2, column=0)
        tk.Button(self.master, text="Close", command=self.master.quit).grid(
            row=2, column=1
        )

    def adjust_width(self, event):
        # Get the current content of the Entry widget
        content = self.code_entry.get()

        # Calculate the new width (the length of the content plus some padding)
        new_width = len(content) + 10

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
        try:
            original_content = read_file_content(self.file_entry.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        try:
            import_meta_class(self.file_entry.get(), self.code_entry.get())
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
            self.code_entry.delete(0, tk.END)  # Clear the text entry widget
            self.code_entry.insert(0, code)  # Insert the code


root = tk.Tk()
gui = GUI(root)
root.mainloop()
root.wm_attributes('-transparentcolor', root['bg'])
