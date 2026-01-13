import time
import TOOLS_COMMON as fgo


'''
    使用这个脚本，规则
        1.助战，筛选，礼装羁绊
        2.公主的礼装随便：
            这里因为术阶初本掉落以下6种，所以带一个加掉落的就行
                1.蛇眼
                2.书页
                3.影尘
                4.甲虫
                5.心脏
                6.魔灯
        3.御主的装备必须 战斗服
        4.参照fgo_relative下的「术阶极本.png」

'''
def main():
    fgo.main_method(rounds,'术阶初级')


def rounds(if_continue):
        
    prepare_buff()
    attack(1,23)

    prepare_buff1()
    attack(1,26)

    fgo.master_buff(1)
    attack(3,20)

    # 结算画面
    fgo.score_screen(if_continue)


def prepare_buff():

    # 阿拉什加宝具值
    fgo.servant_buff(1,3)

    # 梅林 +10宝具值
    fgo.servant_buff(2,2)

    # 源赖光技能2，3
    fgo.servant_buff(3,2)
    fgo.servant_buff(3,3)


def prepare_buff1():
    # saber 技能1，2，3
    fgo.servant_buff(1,1)
    fgo.servant_buff(1,2)
    fgo.servant_buff(1,3)

    # 梅林技能1，3
    fgo.servant_buff(2,1)
    fgo.servant_buff_target(2,3,3)

    # 圣诞公主换下梅林
    fgo.master_buff_sub_off(2,4)

    # 公主技能1，3
    fgo.servant_buff(2,1)
    fgo.servant_buff_target(2,3,3)


def attack(baoju_num,delay=24):
    
    fgo.push_attack_button()
    fgo.baoju_card(baoju_num)
    fgo.rbg_card(1)
    fgo.rbg_card(2)
    time.sleep(delay)


if __name__ == '__main__':
    main()