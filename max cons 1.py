class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,max1=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                if c>max1:
                    max1=c
                c=0
        if c>max1:
            max1=c
        return max1
