class Solution:
    def check(self, nums: List[int]) -> bool:
        k=-9999
        c=0
        for i in range(len(nums)):
            if nums[i]>=nums[i-1]:
                continue
            else:
                c+=1
        if c<=1:
            return True
        else:
            return False
