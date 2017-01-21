class Song():

    def __init__(self, filename, name, bpm, artist=None, description=None):
        self.filename = filename
        self.name = name
        self.bpm = bpm
        self.artist = artist
        self.description = description

    def get_filename(self):
        return self.filename

    def get_name(self):
        return self.name

    def get_bpm(self):
        return self.bpm

    def get_artist(self):
        return self.artist

    def get_description(self):
        return self.description
