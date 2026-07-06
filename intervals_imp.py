class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=0
        arr=[0]*1000000
        intervals.sort(key=lambda x:(x[0],-x[1]))  
        maxend=0      
        for a,b in intervals:
            if b>maxend:
                c+=1
                maxend=b
        return c
