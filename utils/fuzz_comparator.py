from rapidfuzz import fuzz
import os


class FuzzComparator:
    def __init__(self, value: str):
        self.value = value.lower()

    def matches(self, pattern: str) -> bool:
        fuzz_threshold = os.getenv("FUZZ_SIMILARITY_THRESHOLD")
        return fuzz.partial_ratio(pattern.lower(), self.value.lower()) > float(fuzz_threshold)
