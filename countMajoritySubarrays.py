class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cc=0
        for i in range(len(nums)):
            c=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    c+=1
                if c>(j+1-i)//2:
                    cc+=1
                
        return cc
