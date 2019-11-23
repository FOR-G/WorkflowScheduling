from math import pi, asin, sqrt, sin, cos

R = 6371393 #地球半径 米


def rad(d): #将角度转换为弧度
    return d*pi/180.0


# 输入两点经纬度求出两点距离
def getDistance(lati1,longi1,lati2,longi2):
    radLati1 = rad(lati1)
    radLati2 = rad(lati2)
    disLat = radLati1-radLati2
    disLong = rad(longi1)-rad(longi2)
    s = R*asin(sqrt(pow(sin(disLat/2),2)+cos(radLati1)*cos(radLati2)*pow(sin(disLong/2),2)))*R
    return s