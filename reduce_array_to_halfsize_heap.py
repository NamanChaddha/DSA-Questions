class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        minheap=[]
        d={}
        c=0
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        for j in d:
            heapq.heappush(minheap,(-1*d[j],j))
        k=0
        print(minheap)
        while k<  len(arr)//2:
            k+=-1*heapq.heappop(minheap)[0]
            c+=1
        return c
