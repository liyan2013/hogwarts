class Computer:

    def __init__(self):
        self.cpu = "Inter i7"
        self.memory = "8G"
        self.hard_disk = "2TB"
        self.mouse = "罗技鼠标"
        self.keyboard = "达尔优机械键盘"
        self.display = "戴尔显示器"

    def click(self):
        print("单击鼠标:" + self.mouse)

    def double_click(self):
        print("双击鼠标:" + self.mouse)

    def right_click(self):
        print("右击鼠标:" + self.mouse)

    def input_key(self, key):
        print(self.keyboard + "输入:" + key)
