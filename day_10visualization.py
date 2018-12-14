import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
points=[]
with open("data") as file:
    while True:
        line=file.readline()
        if not line:
            break
        points.append([int(i) for i in re.findall("[-]*\d+",line)])
x,y=[i[0] for i in points], [i[1] for i in points]
fig = plt.figure()   
ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(y), max(y)))   
line, = ax.plot([], [], "ro")   
  
# initialization function: plot the background of each frame   
def init():   
    line.set_data([], [])   
    return line,   
  
# animation function.  this is called sequentially   
def animate(i):   
    for i in points:
        i[0]+=i[2]
        i[1]+=i[3]
    x,y=[i[0] for i in points], [i[1] for i in points]
    line.set_data(x, y)   
    return line,   
  
# call the animator.  blit=true means only re-draw the parts that have changed.   
anim = FuncAnimation(fig, animate, init_func=init,   
                               frames=200, interval=2, blit=True) 
    
