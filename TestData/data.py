import random

from model import Location,User,Server

'''
先假设一些数据
坐标（0，0）为中心，半径100
服务器 半径20

'''
locList = []
for i in range(1,11):
    loc = Location(random.uniform(-100.0, 100.0,2),random.uniform(-100.0, 100.0,2))
    loc.print()