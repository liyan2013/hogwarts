class Box:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def pack(self, something):
        print(f"pack {something}")
