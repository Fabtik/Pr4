import tkinter as tk
import database
import app
from database import CalendarDatabase
from app import CalendarApp

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()