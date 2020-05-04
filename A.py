parent = {}
closelst = []
openlst = {}
h = [9,7,1,5,0]
start = 0
dest = 4
i = start
nodes = [[(1,1 ), (2, 2)], [(3, 1)], [(3, 2), (4, 10)], [(4, 5)]]
print('Nodes ' + str(nodes))
parent[i] = 0
openlst[i] = h[i]
while i != dest :
    n = nodes[i]
    openlst.pop(i)
    closelst.append(i)
    for j in n :
        if j[0] in closelst :
            continue
        g = parent.get(i) + j[1]
        fn =  g + h[j[0]]
        if j[0] in openlst :
            if openlst.get(int(j[0])) > fn :
                openlst[j[0]] = fn
        else :
            openlst[j[0]]= fn
        parent[j[0]]= g
    i = min(openlst , key=lambda k: openlst[k])

        
print('parent list: ' + str(parent))
print('open list : ' + str(openlst))
print('close list :' + str(closelst))
print('shortest path : ' + str(parent[4]))
