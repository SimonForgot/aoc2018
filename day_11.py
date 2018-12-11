import numpy as np
from scipy.ndimage import uniform_filter
grid=np.zeros((301,301))
x_list=np.arange(301)
x_grid=np.zeros_like(grid)
x_grid=grid+x_list
y_grid=np.zeros_like(x_grid)
y_grid+=x_grid
x_grid=x_grid.T
x_grid+=10
factor=(x_grid*y_grid+7315)*x_grid
factor//=100
factor-=(factor//10*10)
factor-=5
max_power=-999
maxi=0
max_xy=()
for i in range(1,301):    
    res=uniform_filter(factor, size=i)*i*i
    if i!=1 and i!=2:
        res=res[i//2:-((i-1)//2),i//2:-((i-1)//2)]
    elif i==2:
        res=res[1:,1:]
    if max_power<np.max(res):
        max_power=np.max(res)
        maxi=i
        max_xy=np.where(res==max_power)
print(max_xy,maxi)
