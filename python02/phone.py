class Phone:

    def __init__(self, phone_num, gen):
        # 手机号码
        self.phone_num = phone_num
        # 手机网络（3G, 4G, 5G）
        self.gen = gen

    def call(self, other_num):
        print("call " + str(other_num))

    def send_msg(self, other_num, msg):
        print(f"send message to {other_num}: {msg}")
