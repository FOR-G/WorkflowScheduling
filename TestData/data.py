import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np

from model import Location, User, Server

'''
先假设一些数据
坐标（0，0）为中心，半径100
服务器 半径20
'''


# 产生随机位置
def getRandomLocation():
    x1 = random.uniform(-50.0, 50.0)
    x2 = random.uniform(-50.0, 50.0)
    # loc = Location(x1,x2)
    loc = Location([format(x1, '.2f'), format(x2, '.2f')])
    return loc


# 得到N个位置
def getNPos(N):
    locLi = []
    for i in range(N):
        locLi.append(getRandomLocation())
    return locLi


# 初始化S个服务器并存入Server_data.txt中
def initServer(S):
    ser = []
    for i in range(S):
        radius = random.randint(20,25)
        price = random.randint(5,10)
        s = Server(radius, price,getRandomLocation())
        ser.append(s)
    with open("Server_data.txt", 'w',encoding='utf8') as file:
        for s in ser:
            file.write(str(s)+'\n')
    return ser

# 从Server_data.txt读服务器数据
def getServer():
    ser = []
    with open("Server_data.txt",'r',encoding='utf8') as file:
        for content in file:
            li = content.split()
            s = Server([li[0],li[1]],li[2],li[3])
            # s.print()


# 存入N个用户/工作流


# 画出服务器的为位置
def plotCircle(Li= []):

    fig, ax = plt.subplots()
    N = 50
    n = 20
    x = np.random.uniform(-1 * N, N, size=n)
    y = np.random.uniform(-1 * N, N, size=n)
    r = np.random.randint(20, 25, n)
    c = 20 * np.random.rand(n)  #颜色
    for i in range(len(x)):
        c = pat.Circle((x[i], y[i]), r[i], edgecolor='black', alpha=.5)
        ax.add_patch(c)
    ax.plot()
    # plt.show()        #坐标不自动补全



# plotCircle()
