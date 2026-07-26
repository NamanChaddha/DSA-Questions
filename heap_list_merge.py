# Write solution code here
import heapq
def dij(wlist,s):
    dist={v:float('inf') for v in wlist}
    p={v:None for v in wlist}
    dist[s]=0
    pq=[(0,s)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v,w in wlist[u]:
            if dist[v]>d+w:
                dist[v]=d+w
                p[v]=u 
                heapq.heappush(pq,(dist[v],v))
    return dist,p 
    
def getpath(p,d):
    path=[]
    while d is not None:
        path.append(d)
        d=p[d]
    return path[::-1]
    
def min_cost_walk(wlist,s,d,v):
    dist1,par1=dij(wlist,s)
    dist2,par2=dij(wlist,v)
    path1=getpath(par1,v)
    path2=getpath(par2,d)
    route=path1+path2[1:]
    return (dist1[v]+dist2[d],route)
        
        






size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))
