import re
from treelib import Tree,Node

with open("num") as file:
    nums=[]
    while True:
        line=file.readline()
        if not line:
            break
        nums+=re.findall("\d+",line)
    nums=[int(i) for i in nums]
    
t=0
tree=Tree()
node=Node(tag=0,identifier=0,data=[])
node.identifier=tree.size()+1
tree.add_node(node)
current_node_id=tree.root
#tag用来记录data数量
#identifier用来记录是第几个结点，同时也作为标识
#data存储数据
while t<len(nums):

    #print(tree.nodes)
    n_s=nums[t]
    #如果当前节点为叶节点
    if n_s==0:
        # write tag
        t+=1
        tree.get_node(current_node_id).tag=nums[t]
        have_bro=False
        while have_bro==False:
            #填充data数据
            for i in range(tree.get_node(current_node_id).tag):
                t+=1
                tree.get_node(current_node_id).data.append(nums[t])
            #然后，查找他的没写数据的兄弟节点
            bros=tree.siblings(current_node_id)
            for i in bros:#不知为何在object的list中叠代就可以修改了
                if i.data==[]:
                    have_bro=True
                    current_node_id=i.identifier
                    break
            if have_bro!=True:
                parent=tree.parent(current_node_id)
                if not parent:
                    break
                else:
                    current_node_id=parent.identifier
                   # current_node_id=parent.identifier
    else:
        #不是叶节点的话，创建多个子节点并赋自己的tag
        for i in range(n_s):
            temp_n=Node(tag=0,identifier=tree.size()+1,data=[])
            tree.add_node(temp_n,current_node_id)
        t+=1
        tree.get_node(current_node_id).tag=nums[t]
        current_node_id=tree.get_node(tree.size()-n_s+1).identifier
    t+=1


#tree.show()

#part1
"""
s=0
for value in tree.nodes.values():
    s+=sum(value.data)
print(s)

"""
#part2
def get_value(id):
    value=0
    if len(tree.children(id))!=0:
        for i in tree.get_node(id).data:
            if i>0 and i<=len(tree.children(id)):
                value+=get_value(tree.children(id)[i-1].identifier)
    else:
        for i in tree.get_node(id).data:
            value+=i
    return value
print(get_value(tree.root))
