#446 players; last marble is worth 71522 points
from collections import deque,defaultdict
players_num=446
marbles_num=7152200
scores=defaultdict(int)
circle=deque([0])
for i in range(1,marbles_num+1):
    if i%23==0:
        circle.rotate(7)
        scores[i%players_num]+=i+circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)
print(max(scores.values()))
        
