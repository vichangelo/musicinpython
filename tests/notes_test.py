NATURAL_NOTES = ["C", "D", "E", "F", "G", "A", "B"]
ACCIDENTAL_NOTES = [("C#", "Db"), ("D#", "Eb"), ("F#", "Gb"),
                    ("G#", "Ab"), ("A#", "Bb")]

ALL_NOTE_NAMES = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb",
             "G", "G#", "Ab", "A", "A#", "Bb", "B"]

SHARP_KEYS = ["G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#"]
FLAT_KEYS = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb"]

class Note:
    def __init__(self, name: str):
        if name not in ALL_NOTE_NAMES:
            raise ValueError("Invalid note name.")
        self.name = name
        self.accident_sign = ""

    def is_accidental(self):
        for accident in ACCIDENTAL_NOTES:
            if self.name in accident:
                return True
        return False

    def get_accident_sign(self):
        if self.is_accidental():
            self.accident_sign = self.name[1]

    def is_flat(self):
        if self.is_accidental():
            if self.accident_sign == "b":
                return True
            else:
                return False
        else:
            return False

    def is_sharp(self):
        if self.is_accidental():
            if self.accident_sign == "#":
                return True
            else:
                return False
        else:
            return False

    def enharmonize(self):
        if self.is_accidental():
            for item in ACCIDENTAL_NOTES:
                if self.name in item[0]:
                    return Note(item[1])
                elif self.name in item[1]:
                    return Note(item[0])

class ChromaticScaleGenerator:
    def __init__(self, root: Note):
        self.root = root
        self.notes = []

    def generate_base_scale(self):
        if self.root.name in SHARP_KEYS:
            for note_name in ALL_NOTE_NAMES:
                if "b" not in note_name:
                    self.notes.append(Note(note_name))

        elif self.root.name in FLAT_KEYS:
            for note_name in ALL_NOTE_NAMES:
                if "#" not in note_name:
                    self.notes.append(Note(note_name))

    def generate(self):
        self.generate_base_scale()
        for note in self.notes:
            if note.name == self.root.name:
                index = self.notes.index(note)
        chromatic_scale = (self.notes[index:]
                           + self.notes[:index])
        self.notes = chromatic_scale


def note_input():
    while True:
        try:
            note_input = input("Please insert the note you want to "
                               + "know about. ")
            note = Note(note_input)
        except ValueError:
            print("Invalid note. Please enter one between C and B.\n")
        else:
            return note


def all_about_note():
    note = note_input()
    print("Here's everything about this note:")
    if note.is_accidental():
        accident_notice = "This note is "
        if note.is_flat():
            accident_notice += "flat."
        if note.is_sharp():
            accident_notice += "sharp."
        print(accident_notice)

        enharmonic = note.enharmonize()
        print(f"This note's enharmonic is {enharmonic.name}.")
    else:
        print("This is a natural note.")

    chroma_gen = ChromaticScaleGenerator(note)
    chroma_gen.generate()
    chromatic_scale_names = [note.name for note in chroma_gen.notes]
    chromatic_scale = " ".join(chromatic_scale_names)
    print("This note's chromatic scale is:\n" + chromatic_scale)


if __name__ == "__main__":
    print("\nYou're now into the notes module!")
    while True:
        decision = input("\nEnter 'N' to pick a note to know about "
                         + "or 'B' to go back. ")
        if decision == "N":
            all_about_note()
        if decision == "B":
            break


class TestNoteClass:
    note_natural = Note("H")
    note_sharp = Note("D#")
    note_flat = Note("Db")

    def test_is_accidental(self):
        assert self.note_natural.is_accidental() is False
        assert self.note_sharp.is_accidental() is True
        assert self.note_flat.is_accidental() is True

    def test_get_accident_sign(self):
        self.note_sharp.get_accident_sign()
        self.note_flat.get_accident_sign()
        assert self.note_sharp.accident_sign == "#"
        assert self.note_flat.accident_sign == "b"

    def test_is_flat(self):
        assert self.note_natural.is_flat() is False
        assert self.note_sharp.is_flat() is False
        assert self.note_flat.is_flat() is True

    def test_is_sharp(self):
        assert self.note_natural.is_sharp() is False
        assert self.note_sharp.is_sharp() is True
        assert self.note_flat.is_sharp() is False

    def test_enharmonize(self):
        enharmonized_sharp = self.note_sharp.enharmonize()
        enharmonized_flat = self.note_flat.enharmonize()
        assert enharmonized_sharp.name == "Eb"
        assert enharmonized_flat.name == "C#"


class TestChromaticScaleGeneratorClass:
    note_sharp = Note("D#")
    note_flat = Note("Db")
    sharp_chroma_gen = ChromaticScaleGenerator(note_sharp)
    flat_chroma_gen = ChromaticScaleGenerator(note_flat)

    def test_generate_base_scale(self):
        self.sharp_chroma_gen.generate_base_scale()
        assert self.sharp_chroma_gen.notes[1].name == "C#"

        self.flat_chroma_gen.generate_base_scale()
        assert self.flat_chroma_gen.notes[1].name == "Db"

    def test_generate(self):
        self.sharp_chroma_gen.generate()
        assert self.sharp_chroma_gen.notes[11].name == "D"

        self.flat_chroma_gen.generate()
        assert self.flat_chroma_gen.notes[11].name == "C"
