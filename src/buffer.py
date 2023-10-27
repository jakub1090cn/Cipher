from typing import List, Dict, Any
from dataclasses import asdict
from src.text import Text

class Buffer:
    def __init__(self):
        self.data = []

    def add_text(self, text: Text) -> None:
        self.data.append(text)

    def save_to_file(self, file_name: str) -> None:
        with open(file_name, 'w') as file:
            for item in self.data:
                file.write(f"{item}\n")

    def load_from_file(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.data.append(line.strip())

    def convert_data_to_list_of_dicts(self) -> List[Dict[str, Any]]:
        return [asdict(Text(item.text, item.rot_type, item.status)) for item in self.data]


    def clear_buffer(self) -> None:
        self.data = []
