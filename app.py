import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from database import CalendarDatabase

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний календар з замітками")
        self.db = CalendarDatabase("notes.json")  # Specify the filename

        self.setup_ui()

    def setup_ui(self):
        self.calendar = Calendar(self.root, date_pattern="dd/MM/yyyy")
        self.calendar.pack(padx=10, pady=10)

        self.selected_date = tk.StringVar()
        self.date_label = tk.Label(self.root, textvariable=self.selected_date)
        self.date_label.pack(pady=10)

        self.note_entry = tk.Entry(self.root)
        self.note_entry.pack(pady=10)
        self.add_button = tk.Button(self.root, text="Додати замітку", command=self.add_note)
        self.add_button.pack()

        self.view_button = tk.Button(self.root, text="Переглянути замітки", command=self.view_notes)
        self.view_button.pack()

        self.calendar.bind("<<DateSelected>>", self.on_date_selected)

    def on_date_selected(self, event):
        self.selected_date.set(self.calendar.get_date())

    def add_note(self):
        selected_date_str = self.calendar.get_date()
        note = self.note_entry.get()
        self.db.add_note(selected_date_str, note)
        self.note_entry.delete(0, tk.END)

    def view_notes(self):
        selected_date_str = self.calendar.get_date()
        notes = self.db.get_notes(selected_date_str)
        if notes:
            note_list = "\n".join(notes)
            message = f"Замітки для {selected_date_str}:\n{note_list}"
            messagebox.showinfo("Замітки", message)
        else:
            messagebox.showinfo("Замітки", f"Заміток для {selected_date_str} немає.")