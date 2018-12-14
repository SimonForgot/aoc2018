import random
import sys
from PIL import Image
import re
from collections import defaultdict
def distance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)
    #return  (x2-x1)**2+(y2-y1)**2
def find_nearest_color(x,y):
    #return (0,0,0)
    nearst_distance=sys.maxsize
    return_i=-1
    for i in points:
        dis=distance(x,y,i[0],i[1])
        if dis<nearst_distance:
            nearst_distance=dis
            return_i=i
    for i in points:
        dis=distance(x,y,i[0],i[1])
        if dis==nearst_distance and i!=return_i: 
            return (255,255,255)       
    return return_i[2]
points=[]
with open("data") as file:
    while True:
        line=file.readline()
        if not line:
            break
        points.append([int(i) for i in re.findall("\d+",line)])
        points[len(points)-1].append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
max_x=max(i[0] for i in points)
max_y=max(i[1] for i in points)
img = Image.new("RGB",(max_x+50,max_y+50))
for i in range(max_x+50):
    for j in range(max_y+50):
        nc=find_nearest_color(i,j)
        img.putpixel((i,j),nc)
color_num=defaultdict(int)  
for i in range(max_x+50):
    for j in range(max_y+50):
        color_num[img.getpixel((i,j))]+=1
for i in range(max_x+50):
    for j in range(max_y+50):
        if i==0 or i==max_x+50-1 or j==0 or j==max_y+50-1:
            if img.getpixel((i,j)) in color_num.keys():
                color_num.pop(img.getpixel((i,j)))
for i in range(max_x+50):
    for j in range(max_y+50):
        if img.getpixel((i,j)) not in color_num:
            img.putpixel((i,j),(255,255,255))    
img.save("vonoroi.png")
print(max(color_num.values()))
