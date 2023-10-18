class Manager:
    def __init__(self, buffer, file_handler):
        self.buffer = buffer
        self.file_handler = file_handler

    def encrypt_text(self, text, rot_type):
        encrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset + rot_type) % 26 + ascii_offset)
                encrypted_text += decrypted_char
            else:
                encrypted_text += char
        return encrypted_text


    def decrypt_text(self, text, rot_type):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - rot_type) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

    def save_to_file(self, file_name, append=False):
        self.file_handler.write_to_file(file_name, self.buffer.data, append)

    def load_from_file(self, file_name):
        self.buffer.clear_buffer()
        data = self.file_handler.read_from_file(file_name)
        if data:
            for item in data:
                self.buffer.add_text(item)

    def clear_buffer(self):
        self.buffer.clear_buffer()



