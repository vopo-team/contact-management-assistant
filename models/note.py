from field import Field
from tag import Tag
from rapidfuzz import fuzz

class Note(Field):
    __MIN_NOTE_LENGTH = 1
    __MAX_NOTE_LENGTH = 200
    __TAG_SEPARATOR = " "
    __FUZZ_SIMILARITY_THRESHOLD = 80

    def __init__(self, text: str):
        self.__validate(text)
        self.tags = []
        super().__init__(text)

    def has_tag(self, tag: Tag) -> bool:
        return tag in self.tags
    
    def has_pattern(self, pattern: str) -> bool:
        return fuzz.partial_ratio(pattern.lower(), self.value.lower()) > self.__FUZZ_SIMILARITY_THRESHOLD

    def add_tag(self, tag: Tag) -> str:
        if self.has_tag(tag):
            return "Tag already exists"
        self.tags.append(tag)
        return "Tag added."
    
    def remove_tag(self, tag: Tag) -> str:
        if not self.has_tag(tag):
            return "Note hasn't this tag"
        self.tags.remove(tag)
        return "Tag removed."
    
    def edit_tag(self, target_tag: Tag, new_tag: Tag) -> str:
        if not self.has_tag(target_tag):
            return "Target tag doesn't exist"
        if self.has_tag(new_tag):
            return "The new tag name is already reserved."
        target_index = self.tags.index(target_tag)
        self.tags[target_index] = new_tag

        return f"Tag {target_index} renamed to {new_tag}"

    def all_tags(self) -> str:
        return f"{self.__TAG_SEPARATOR.join(str(p) for p in self.tags)}"


    @classmethod
    def __validate(cls, value: str):
        if len(value) >= cls.__MAX_NOTE_LENGTH:
            raise ValueError(f"Note cannot exceed {cls.__MAX_NOTE_LENGTH} characters")
        if len(value) <= cls.__MIN_NOTE_LENGTH:
            raise ValueError(f"Note cannot be less than {cls.__MIN_NOTE_LENGTH} character")

note = Note('VDsfsdfsdfsdff')
note.add_tag(Tag('Dev'))
note.add_tag(Tag('Design'))
print(note.all_tags())