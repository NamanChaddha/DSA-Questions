class Solution:
    def frequencySort(self, s: str) -> str:
        minheap=[]
        d={}
        lst=[]
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in d:
            heapq.heappush(minheap,(d[i],i))
        while minheap:
            val,i=heapq.heappop(minheap)
            lst.append(val*i)
        lst=lst[::-1]
        return ''.join(lst)
        
