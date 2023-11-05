import json

class CalendarDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_note(self, date, note, important=False):
        if date in self.data:
            self.data[date].append({"note": note, "important": important})
        else:
            self.data[date] = [{"note": note, "important": important}]
        self.save_to_file()

    def get_notes(self, date):
        notes = self.data.get(date, [])
        return [(note["note"], note.get("important", False)) for note in notes]

    def delete_notes(self, date):
        if date in self.data:
            del self.data[date]
            self.save_to_file()
