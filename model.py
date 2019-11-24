'''
用户对应工作流，用户位置随机生成，工作流数据给定
工作流为顺序结构 list[t1,t2,t3,t4]
服务器 位置、覆盖范围、价格给定
'''


class Location:
    # longitude 经度 latitude 维度
    def __init__(self, lati=0, longi=0):
        self.latitude = lati
        self.longitude = longi

    def __str__(self):
        return str(self.latitude)+' '+str(self.longitude)

    def print(self):
        print('[' + str(self) + ']')


class User(Location):
    # workflow 只考虑顺序结构 列表表示
    def __init__(self, lati, longi, workf=[]):
        super(User, self).__init__(lati, longi)
        self.workflow = workf

    def __str__(self):
        return str(self.latitude)+' '+str(self.longitude)+' '+str(self.workflow)

    def print(self):
        print('['+str(self)+']')


class Server(Location):
    # 服务器包含位置 价格 范围
    def __init__(self, radius, cost, lati, longi):
        super(Server, self).__init__(lati, longi)
        self.ra = radius
        self.cost = cost

    def __str__(self):
        return str(self.latitude)+' '+str(self.longitude)+' '+str(self.ra)+' '+str(self.cost)

    def print(self):
        print('[' + str(self) + ']')
'''编码'''
# 任务编码，
