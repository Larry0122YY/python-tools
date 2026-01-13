import time
import TOOLS_COMMON as fgo


'''
    使用这个脚本，规则
        1.助战，筛选，礼装羁绊
        2.公主的礼装随便：
            这里因为术阶初本掉落以下三种，所以带一个加掉落的就行
                1.蛇眼
                2.书页
                3.影尘
        3.御主的装备随便选
        4.参照fgo_relative下的「术阶初本.png」

'''
def main():
    fgo.main_method(rounds,'术阶初级')


def rounds(if_continue):
        
    prepare_buff()

    attack(1,23)

    # 这时候圣诞公主上来了，用个技能1
    fgo.servant_buff(1,1)
    attack(2,26)

    attack(3,20)

    # 结算画面
    fgo.score_screen(if_continue)


def prepare_buff():

    # 阿拉什加宝具值
    fgo.servant_buff(1,3)

    # saber 技能3
    fgo.servant_buff(2,3)

    # 源赖光技能2
    fgo.servant_buff(3,2)


def attack(baoju_num,delay=24):
    
    fgo.push_attack_button()
    fgo.baoju_card(baoju_num)
    fgo.rbg_card(1)
    fgo.rbg_card(2)
    time.sleep(delay)


if __name__ == '__main__':
    main()