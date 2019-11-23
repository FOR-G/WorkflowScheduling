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

    def print(self):
        print('[' + str(self.latitude) + ' ' + str(self.longitude) + ']')


class User(Location):
    # workflow 只考虑顺序结构 列表表示
    def __init__(self, lati, longi, workf):
        super(User, self).__init__(lati, longi)
        self.workflow = workf


class Server(Location):
    # 服务器包含位置 价格 范围
    def __init__(self, radius, cost, lati=0, longi=0):
        super(Server, self).__init__(lati, longi)
        self.radius = radius
        self.cost = cost


'''编码'''
# 任务编码，
