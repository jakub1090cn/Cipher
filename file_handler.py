import json
class FileHandler:
    @staticmethod
    def read_from_file(file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f'File {file_name} not found.')

    @staticmethod
    def write_to_file(file_name, data, append=False):
        mode = 'a' if append else 'w'
        with open(file_name, mode) as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def clear_file(file_name):
        with open(file_name, 'w'):
            pass


