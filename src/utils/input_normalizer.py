class InputNormalizer:
    def __init__(self, input_text: str):
        self._normalized = InputNormalizer._normalize(input_text)

    @classmethod
    def _normalize(cls, value: str) -> str:
        return str(value).strip().lower()

    def __str__(self):
        return self._normalized
