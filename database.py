import json

class CalendarDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.notes = {}
        self.load_notes()

    def add_note(self, date, note):
        if date in self.notes:
            self.notes[date].append(note)
        else:
            self.notes[date] = [note]
        self.save_notes()

    def get_notes(self, date):
        return self.notes.get(date, [])

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file)

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = {}