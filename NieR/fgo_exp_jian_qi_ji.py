import time
import TOOLS_COMMON as fgo


'''
    使用这个脚本，规则
        1.剑骑极EXP图片参照
        2.助战，筛选，礼装羁绊
        3.助战，25友情的好友在第一个的
        4.御主礼装无所谓

'''
def main():
    fgo.main_method(rounds,'剑骑极EXP')


def rounds(if_continue):
        
    prepare_buff()

    attack(1,23)

    #源赖光2
    fgo.servant_buff(1,2)
    attack(1,26)

    attack(3,20)

    # 结算画面
    fgo.score_screen(if_continue)


def prepare_buff():

    # 阿拉什3
    fgo.servant_buff(1,3)

    # 梅林1，3
    fgo.servant_buff(2,1)
    fgo.servant_buff(2,2)
    fgo.servant_buff_target(2,3,3)

    # 山中老人1，2，3
    fgo.servant_buff(3,1)
    fgo.servant_buff(3,2)
    fgo.servant_buff(3,3)


def attack(baoju_num,delay=24):
    
    fgo.push_attack_button()
    fgo.baoju_card(baoju_num)
    fgo.rbg_card(1)
    fgo.rbg_card(2)
    time.sleep(delay)


if __name__ == '__main__':
    main()