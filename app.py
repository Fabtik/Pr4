import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from database import CalendarDatabase

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний календар з замітками")
        self.db = CalendarDatabase("notes.json")  # Вкажіть ім'я файлу бази даних

        self.setup_ui()

    def setup_ui(self):
        self.calendar = Calendar(self.root, date_pattern="dd/MM/yyyy")

        # Змінити колір фону віджета tkcalendar
        self.calendar.calevent_bg = "light blue"

        self.calendar.pack(padx=10, pady=10)

        self.selected_date = tk.StringVar()
        self.date_label = tk.Label(self.root, textvariable=self.selected_date)

        # Змінити колір тексту для мітки з датою
        self.date_label.config(fg="red")

        self.date_label.pack(pady=10)

        self.note_entry = tk.Entry(self.root)
        self.note_entry.pack(pady=10)
        self.add_button = tk.Button(self.root, text="Додати замітку", command=self.add_note)

        # Змінити колір фону і тексту для кнопки "Додати замітку"
        self.add_button.config(bg="green", fg="white")

        self.add_button.pack()

        self.view_button = tk.Button(self.root, text="Переглянути замітки", command=self.view_notes)

        # Змінити колір фону і тексту для кнопки "Переглянути замітки"
        self.view_button.config(bg="blue", fg="white")

        self.view_button.pack()

        self.calendar.bind("<<DateSelected>>", self.on_date_selected)

    def on_date_selected(self, event):
        self.selected_date.set(self.calendar.get_date())

    def add_note(self):
        selected_date_str = self.calendar.get_date()
        note = self.note_entry.get()

        if not note:
            messagebox.showerror("Помилка", "Поле замітки не може бути порожнім.")
        else:
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

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()