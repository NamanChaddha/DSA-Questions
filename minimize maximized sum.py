class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        max1=0
        while i<j:
            if nums[i]+nums[j]>max1:
                max1=nums[i]+nums[j]
            i+=1
            j-=1
        return max1