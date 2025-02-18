from datetime import datetime

class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str ):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] =[]

    def add_tags(self, tag: str ):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return (f"Date: {self.creation_date}"
               f"{self.title}: {self.text}")


