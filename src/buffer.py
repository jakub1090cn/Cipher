class Buffer:
    def __init__(self):
        self.data = []

    def add_text(self, text):
        self.data.append(text)

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for item in self.data:
                file.write(f"{item}\n")

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.data.append(line.strip())

    def clear_buffer(self):
        self.data = []
