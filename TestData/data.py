import random
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
from matplotlib.collections import PatchCollection

from model import Location, User, Server

'''
先假设一些数据
坐标（0，0）为中心，半径100
服务器 半径20

'''

# locList = []


# 产生随机位置
def getRandomLocation():
    x1 = random.uniform(-50.0, 50.0)
    x2 = random.uniform(-50.0, 50.0)
    # loc = Location(x1,x2)
    loc = Location(format(x1, '.2f'), format(x2, '.2f'))
    return loc


# 得到N个位置
def getNPos(N):
    locLi = []
    for i in range(N):
        locLi.append(getRandomLocation())
    return locLi


# 存入N个服务器的数据
def saveServer(N):
    server = []
    for i in range(N):
        ser = Server(random.randint(20, 25), random.randint(10, 25),getRandomLocation().latitude,getRandomLocation().longitude, )
        server.append(ser)
    with open("Server_data.txt", 'w',encoding='utf8') as file:
        for s in server:
            file.write(str(s)+'/n')

# saveServer(10)
# 存入N个用户/工作流





# 画出服务器的为位置
def plotCircle(Li= []):
    patch = []
    x = np.linspace(-100, 100, 20)
    y = np.linspace(-100, 100, 20)
    fig, ax = plt.subplots(figsize=(-50, 50), dpi=10)
    for i in Li:
        circle = patches.Circle((i.latitude, i.longitude), 20, color="#BBFFFF", alpha=0.2)
        patch.append(circle)
    collection = PatchCollection(patch)
    ax.add_collection(collection)
    plt.show()

#
# for i in range(1, 11):
#     locList.append(getRandomLocation())
# plotCircle(locList)


