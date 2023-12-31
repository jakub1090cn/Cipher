from src.file_handler import FileHandler
from src.buffer import Buffer
from rot import Rot
from text import Text
import os
# TYPING.


class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.file_handler = FileHandler()
        self.menu = {
            1: 'Encrypt Text',
            2: 'Decrypt Text',
            3: 'Save to File',
            4: 'Load from File',
            5: 'Clear Buffer',
            6: 'Exit'
        }

    def save_to_file(self, file_name: str) -> None:
        file_name = f"{file_name}.json"
        data_to_write = self.buffer.convert_data_to_list_of_dicts()
        if os.path.isfile(file_name):
            self.file_handler.append_to_file(file_name, data_to_write)
        else:
            self.file_handler.write_to_file(file_name, data_to_write)

    def load_from_file(self, file_name: str) -> None:
        self.buffer.clear_buffer()
        data = self.file_handler.read_from_file(file_name)
        if data:
            for item in data:
                self.buffer.add_text(item)

    def clear_buffer(self):
        self.buffer.clear_buffer()

    @staticmethod
    def rot_type2rot(rot_type: str) -> int:
        rot_mapping = {'rot13': 13, 'rot47': 47}
        return rot_mapping.get(rot_type)

    def run(self):
        while True:
            for idx, action in self.menu.items():
                print(f'{idx} -- {action}')
            choice = int(input('Enter your choice: '))
            match choice:
                case 1:
                    text = input('Enter text to encrypt: ')
                    rot_type = input('Enter type of encryption (rot13 or rot47): ')
                    rot = self.rot_type2rot(rot_type)
                    encrypted = Rot.encrypt_text(text, rot)
                    text_object = Text(text=encrypted, rot_type=rot_type, status='Encrypted')
                    self.buffer.add_text(text_object)
                    print(encrypted)


                case 2:
                    text = input('Enter text to decrypt: ')
                    rot_type = input('Enter type of decryption (rot13 or rot47): ')
                    rot = self.rot_type2rot(rot_type)
                    decrypted = Rot.decrypt_text(text, rot)
                    text_object = Text(text=decrypted, rot_type=rot_type, status='Decrypted')
                    self.buffer.add_text(text_object)
                    print(decrypted)

                case 3:
                    file_name = input('Enter the file name to save to (without extensions): ')
                    self.save_to_file(file_name)
                case 4:
                    file_name = input('Enter the file name to load from: ')
                    self.load_from_file(file_name)
                case 5:
                    self.clear_buffer()
                case 6:
                    exit()


    
    
    
    
    
    
