class TongLao:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == "无崖子":
            print("师弟！！！")
        elif name == "李秋水":
            print("呸！见人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("你是谁?")

    def fight_zms(self, hp, power):
        # 不明白血量缩减2倍是什么意思，就将血量降为1/2
        self.hp = self.hp / 2
        self.power = self.power * 10

        self.hp = self.hp - power
        enemy_hp = hp - self.power
        if self.hp > enemy_hp:
            print("我赢了")
        elif self.hp < enemy_hp:
            print("敌人赢了")
        else:
            print("平手")


class XuZhu(TongLao):

    def __init__(self, hp, power):
        TongLao.__init__(self, hp, power)

    def read(self):
        print("罪过罪过")


if __name__ == '__main__':
    tonglao = TongLao(1000, 50)
    tonglao.fight_zms(1000, 20)

    xuzhu = XuZhu(1000, 50)
    xuzhu.read()
