import time
import TOOLS_COMMON as fgo


'''
    使用这个脚本，规则
        1.一定要用exp那个组
        2.助战，筛选，礼装羁绊
        3.助战，25友情的好友在第一个的

'''
def main():
    fgo.main_method(rounds,'经验值')


def rounds(if_continue):
        
    prepare_buff()

    attack(1,23)
    attack(2,26)

    # 唐僧的宝具增强技能只有一回合，所以必须在这里使用
    fgo.servant_buff(3,1)
    attack(3,20)

    # 结算画面
    fgo.score_screen(if_continue)


def prepare_buff():

    # 圣诞公主技能1,3
    fgo.servant_buff(1,1)
    fgo.servant_buff_target(1,3,2)

    # 圣诞公主和saber换人
    fgo.master_buff_sub_off(1,4)

    # saber 技能1，2，3
    fgo.servant_buff(1,1)
    fgo.servant_buff(1,2)
    fgo.servant_buff(1,3)

    # 源赖光技能2
    fgo.servant_buff(2,2)

    # 唐僧技能2
    fgo.servant_buff(3,2)


def attack(baoju_num,delay=24):
    
    fgo.push_attack_button()
    fgo.baoju_card(baoju_num)
    fgo.rbg_card(1)
    fgo.rbg_card(2)
    time.sleep(delay)


if __name__ == '__main__':
    main()