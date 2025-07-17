class InputNormalizer:
    def __init__(self, input_text):
        self._normalized = self.__normalize(input_text)

    @staticmethod
    def __normalize(value) -> str:
        if value is None:
            return ""  # Normalize None to empty string
        return str(value).strip().lower()

    def __str__(self):
        return self._normalized
