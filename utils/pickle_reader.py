import pickle
from models.contact_book import ContactBook

class PickleReader:
    __WRITE_ACTION = "wb"
    __READ_ACTION = "rb"

    @staticmethod
    def save_data(book, filename):
        with open(filename, PickleReader.__WRITE_ACTION) as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(filename) -> ContactBook:
        try:
            with open(filename, PickleReader.__READ_ACTION) as f:
                return pickle.load(f)
        except FileNotFoundError:
            return ContactBook()