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
    def write_to_file(file_name, data):
        _data = {'data': data}
        with open(file_name, 'w') as file:
            json.dump(_data, file, indent=4)

    @staticmethod
    def append_to_file(file_name, data):
        loaded_data = FileHandler.read_from_file(file_name)
        new_data = loaded_data['data'] + data
        FileHandler.write_to_file(file_name, new_data)

    @staticmethod
    def clear_file(file_name):
        with open(file_name, 'w'):
            pass


