import pickle

from models import ContactBook


class PickleReader:
    WRITE_ACTION = "wb"
    READ_ACTION = "rb"

    @staticmethod
    def save_data(book, filename: str):
        with open(filename, PickleReader.WRITE_ACTION) as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(filename: str) -> ContactBook:
        try:
            with open(filename, PickleReader.READ_ACTION) as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return ContactBook()
