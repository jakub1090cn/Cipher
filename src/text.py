
from dataclasses import dataclass, asdict


@dataclass
class Text:
    text: str
    rot_type: str
    status: str

    def __str__(self):
        return f'Text: {self.text}\nType: {self.rot_type}\nStatus: {self.status}'
