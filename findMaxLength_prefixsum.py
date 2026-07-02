class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n0=0
        n1=0
        c=0
        ans=0
        max1=0
        d={}
        for i in range(len(nums)):
            if nums[i]==1:
                n1+=1
            else:
                n1-=1
            if n1==0:
                ans=i+1
            elif n1 in d:
                anss=i-d[n1]
                if anss>ans:
                    ans=anss
            else:
                d[n1]=i
        return ans
