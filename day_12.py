initial_state="###......#.#........##.###.####......#..#####.####..#.###..#.###.#..#..#.#..#..#.##...#..##......#.#"
initial_state=10*"."+initial_state+3000*"."

rule=[]
rules=[]
with open("data") as file:
    while True:
        line=file.readline()
        if not line:
            break
        rule.append(line)
for i in rule:
    rules.append((i[0:5],i[9]))
del rule

change=[]
for i in range(len(initial_state)):
    change.append(26)
change=[26,26]+change[:-2]
generation=2000    
os=0
for t in range(1,generation+1): 
    for index,s in enumerate(rules):
        start=0
        find_loc=initial_state.find(s[0],start)
        while find_loc!=-1:
            change[find_loc+2]=index
            start=find_loc
            find_loc=initial_state.find(s[0],start+1)
    for i in range(len(change)):
        initial_state=list(initial_state)
        initial_state[i]=rules[change[i]][1]
        initial_state="".join(initial_state)
    ns=0
    for index,i in enumerate(initial_state):
        if i=='#':
            ns+=(index-10)   
    if t==150:            
        print(ns-os)    
        print(ns)
        break
    os=ns       
            
"""
(50000000000-150)*42+6728
Out[2]: 2100000000428
"""
        

