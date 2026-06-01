class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        s=cost
        c=0
        s.sort()
        while len(s)>2:
            c+=s[-1]+s[-2]
            s.pop(-1)
            s.pop(-1)
            s.pop(-1)
        else:
            c+=sum(s)
            s=[]
        return c
