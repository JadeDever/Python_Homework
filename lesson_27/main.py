# 别忘了在这里导入必要的模块哦
import card
from random import choice


class Role:
    def build(self, card, skill):
        self.card = card
        self.skill = skill

    def show_card(self):
        print(''' 你的身份卡是：
    %s
          你拥有的技能是：%s
          ''' % (self.card, self.skill))

# 狼人阵营


class Wolf(Role):
    def __init__(self):
        self.build(card.wolf_symbol, '每晚可和同伴一起杀死一名玩家')

# 人类阵营


class Human(Role):
    pass


# 预言家是人类阵营
# 每晚可查验任意一名在座玩家的身份
class Prophet(Human):
    def __init__(self):
        self.build(card.prophet_symbol, '每晚可查验任意一名在座玩家的身份')

# 女巫是人类阵营
# 有一瓶毒药、一瓶解药


class Witch(Human):
    def __init__(self):
        self.build(card.witch_symbol, '有一瓶毒药、一瓶解药')


# 猎人是人类阵营
# 被投票出局或中刀身亡时，可开枪带走任意一名玩家
class Hunter(Human):
    def __init__(self):
        self.build(card.hunter_symbol, '被投票出局或中刀身亡时，可开枪带走任意一名玩家')

# 村民是人类阵营
# 没有特殊技能


class Villager(Human):
    def __init__(self):
        self.build(card.villager_symbol, '没有特殊技能')


# 狼人杀九人局标准配置：3 狼、3 村民、1 预言家、1 女巫、1 猎人
roles = [Wolf(), Wolf(), Wolf(),
         Villager(), Villager(), Villager(),
         Hunter(), Prophet(), Witch()]
# 游戏开始时，你可从所有角色牌中抽取一张，作为自己的身份卡
myRole = choice(roles)
# 请调用 show_card() 方法，观察自己的角色卡
myRole.show_card()
