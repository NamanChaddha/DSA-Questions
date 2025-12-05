class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cz=0
        for i in range(len(nums)-1):
            s1=nums[0:i+1]
            s2=nums[i+1:len(nums)]
            if (sum(s1)-sum(s2))%2==0:
                cz+=1
            else:
                continue
        return cz