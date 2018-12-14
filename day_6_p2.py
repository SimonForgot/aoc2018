
import re
from collections import defaultdict 
def distance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

points=[]
with open("data") as file:
    while True:
        line=file.readline()
        if not line:
            break
        points.append([int(i) for i in re.findall("\d+",line)])
res=0
d=defaultdict(int)
for i in range(400):
    for j in range(400):
        for n in points:
            d[(i,j)]+=distance(i,j,n[0],n[1])
        if d[(i,j)]<10000:
            res+=1
print(res)
