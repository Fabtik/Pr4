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

    def add_note(self, date, note):
        if date in self.data:
            self.data[date].append(note)
        else:
            self.data[date] = [note]
        self.save_to_file()

    def get_notes(self, date):
        return self.data.get(date, [])

    def delete_notes(self, date):
        if date in self.data:
            del self.data[date]
            self.save_to_file()
