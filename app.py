import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from database import CalendarDatabase

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний календар з замітками")
        self.db = CalendarDatabase("notes.json")

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TButton', foreground='black', background='red')  # Установите красный цвет фона для кнопок
        style.configure('TLabel', foreground='red')
        style.configure('TEntry', background='light gray')
        style.configure('TFrame', background='white')

        ttk.Frame(self.root, style='TFrame').grid(row=0, column=0, padx=10, pady=10, rowspan=5, columnspan=3)

        self.calendar = Calendar(self.root, date_pattern="dd/MM/yyyy")
        self.calendar.calevent_bg = "light blue"
        self.calendar.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.note_entry = ttk.Entry(self.root, style='TEntry')
        self.note_entry.grid(row=1, column=0, pady=10, columnspan=3)

        ttk.Button(self.root, text="Додати замітку", command=self.add_note, style='TButton').grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Переглянути замітки", command=self.view_notes, style='TButton').grid(row=2, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Видалити замітки", command=self.delete_notes, style='TButton').grid(row=3, column=0, columnspan=2, pady=10)

        self.date_label = ttk.Label(self.root, text="", style='TLabel')
        self.date_label.grid(row=4, column=0, pady=10, columnspan=3)

        self.calendar.bind("<<DateSelected>>", self.on_date_selected)

    def on_date_selected(self, event):
        self.date_label.config(text=self.calendar.get_date())

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

    def delete_notes(self):
        selected_date_str = self.calendar.get_date()
        response = messagebox.askyesno("Підтвердження видалення", f"Ви впевнені, що хочете видалити замітки для {selected_date_str}?")
        if response:
            self.db.delete_notes(selected_date_str)
            messagebox.showinfo("Успішно", f"Замітки для {selected_date_str} були видалені.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()