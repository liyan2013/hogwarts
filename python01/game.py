import random


def game():
    # 我的血量
    my_hp = 1000
    # 敌人的血量
    enemy_hp = 1000

    while True:
        # 我受到随机的攻击，减少血量
        my_hp = my_hp - random.randint(0, 50)
        # 敌人收到随机的攻击，减少血量
        enemy_hp = enemy_hp - random.randint(0, 50)

        if my_hp <= 0:
            # 如果我此时的血量<=0，则敌人赢了
            print("敌人赢了")
            # 退出循环
            break
        elif enemy_hp <= 0:
            # 如果敌人此时的血量<=0，则我赢了
            print("我赢了")
            # 跳出循环
            break


if __name__ == '__main__':
    game()
