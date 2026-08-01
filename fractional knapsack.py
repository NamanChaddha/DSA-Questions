class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        import heapq
        #code here
        s=[]
        for i in range(len(val)):
            heapq.heappush(s,[-val[i]/wt[i],val[i],wt[i]])
        total=0
        t=[]
        while capacity>0 and s:
            t=heapq.heappop(s)
            if capacity-t[2]>=0:
                capacity-=t[2]
                total+=t[1]
            else:
                total+=((capacity/t[2])*t[1])
                break
        return total
                
