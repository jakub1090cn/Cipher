
class Rot:
    @staticmethod
    def encrypt_text(text: str, rot: int) -> str:
        encrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + rot) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def decrypt_text(text: str, rot_type: int):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - rot_type) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
