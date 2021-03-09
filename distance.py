from math import *

def distance(xA,xB,yA,yB):
    the_distance = sqrt(pow((xA-xB),2)+pow((yA-yB),2))
    print(f"The distance between A({xA},{xB}) and B({yA},{yB}) is : {the_distance}")

print("The first point :")
xA = int(input("xA = ? :"))
xB = int(input("xB = ? :"))

print("The second point :")
yA = int(input("yA = ? :"))
yB = int(input("yB = ? :"))

distance(xA,xB,yA,yB)