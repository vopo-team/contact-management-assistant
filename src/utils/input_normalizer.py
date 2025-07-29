class InputNormalizer:
    def __init__(self, input_text: str):
        self._normalized = self.__normalize(input_text)

    @staticmethod
    def __normalize(value: str) -> str:
        return str(value).strip().lower()

    def __str__(self):
        return self._normalized
