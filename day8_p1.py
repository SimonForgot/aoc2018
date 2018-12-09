from treelib import Node, Tree
import re
nums=[]
with open("data") as file:
    line=file.readline()
    nums=re.findall("\d+",line)
    nums=[int(i) for i in nums]
#nums以list的形式存储input数据

t=0
tree=Tree()
head=Node("header")
tree.add_node(head)
print(tree.size())

print(2)
