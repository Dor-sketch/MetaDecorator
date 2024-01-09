"""
This file contains the GUI for the Meta Class Modifier.
It uses tkinter to create the GUI.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os  # used to get the current directory
from PIL import Image, ImageTk  # Import from Pillow

from meta import (
    read_file_content,
    restore_file_content,
    import_meta_class,
)


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
        self.file_entry = tk.Entry(self.master)
        self.file_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Browse",
                  command=self.browse,).grid(row=0, column=2)

        tk.Label(self.master, text="Enter python code:").grid(row=1, column=0)
        self.code_entry = tk.Entry(self.master)
        self.code_entry.grid(row=1, column=1)

        tk.Button(self.master, text="Run",
                  command=self.run).grid(row=2, column=0)
        tk.Button(self.master, text="Close", command=self.master.quit).grid(
            row=2, column=1
        )

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


root = tk.Tk()
gui = GUI(root)
root.mainloop()
root.wm_attributes('-transparentcolor', root['bg'])
