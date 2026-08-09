class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        c=1
        depths=[0]*len(parent)
        depths[0]=1
        h=0
        def depth(i):
            if depths[i]!=0:
                return depths[i]
            depths[i]=depth(parent[i])+1
            return depths[i]
        for i in range(len(parent)):
            h=max(h,depth(i))
        c=0
        for i in range(len(parent)):
            c+=nums[i]*(h-depth(i)+1)
        return c
