import time
from sympy import Symbol, symbols, solve,Eq,Rational
import math
import matplotlib.pyplot as plt


def main():
    
    exe_frame(fangcheng)


def fangcheng():

    x,y,z = symbols('x y z')

    fangcheng = [x*3 + x/3 - 100]
    fangcheng = [x/20 + x/30 + x/42 - 3]
    fangcheng = [x*2 - 14]
    fangcheng = [x-y-7,4*x+2-7+x]
    fangcheng = [x**2 - 6,x*y-18]
    fangcheng = [2*x+2-3*x+2]
    fangcheng = [(x-2)/3 + (x-3)/5 + (x-2)/7 + (x-5)/9 + (x-1)/11 - 18 ]
    fangcheng = [(x-59)/21 + (x-34)/23 + (x-5)/25 - 6 ]
    fangcheng = [x/0.7 - (0.17-0.2*x)/0.03 - 2 ]
    fangcheng = [10*x/7 - (17-20*x)/3 - 2 ]
    fangcheng = [32 + (x+5)*3 - 45 - 23]
    fangcheng = [(x-57)/11 + (x-42)/13 + (x-23)/15 + x/17 - 10 ]
    fangcheng = [x+15+30+y-180,x+y-135]
    fangcheng = [9*x+5*y-73]
    fangcheng = [x*(x-y)-60,y*(x-y)-24]
    fangcheng = [28*x+y*30+ z*31 -360]
    fangcheng = [x**2+y**2-3**2,(5-x)**2+ y**2-4**2]


    result = solve(
        fangcheng,
        [x,y]
    )



    print(result)

    # # print()
    # print('caculation!!!')
    # print(expr)
    # print(expr.subs(result))


def test():
    pass


def kenengxing():
    range_count = 366
    for i in range(range_count):
        for j in range(range_count):
            for k in range(range_count):
                c = i*29 + j*30+k*31 == 366
                
                if c:
                    print(f'答案是{i+j+k},{i},{j},{k}')


def  suan_math1():
    range_count = 1080
    for i in range(range_count):
        a = int(f'{i}{i}')
        b = int(f'{i}{i}{i}')

        c = i*2 + a*2 + b == range_count

        if c:
            print(f'{i}')


def suan_math2():
    range_count = 1080
    for i in range(range_count):
        for j in range(range_count):
            a = int(f'{i}{j}')
            b = int(f'{j}{i}')
            c = a + b ==range_count
            
            if c:
                print(f'{i}和{j},他们的和是{i+j}')


def suan_math3():
    range_count = 777
    for i in range(range_count):
        for j in range(range_count):
            for k in range(range_count):
                a = int(f'{i}{j}{k}')
                b = int(f'{i}{j}{j}')
                c = a + b == range_count
                
                if c:
                    print(f'{i}和{j}和{k}')





def exe_frame(method):
    time_start = time.perf_counter()

    method()

    time_end = time.perf_counter()

    time_cost = time_end - time_start
    cost_min = int(int(time_cost//60))
    cost_sec = time_cost % 60
    print(f'花费时间：{cost_min}分{cost_sec:.2f}秒')

    
def t260105():
    for i in range(10):
        c = i*3 + int(str(i)+str(i)) +int(str(i)+str(i)+str(i))

        if c == 500:
            print(i)


def er_de_cifang_xiangjia():
    result = 0
    for i in range(101):
        result += 2**i

        print(result)

        sss = 2**101 -1

        if result == sss:
            print(True)



if __name__ == '__main__':
    main()