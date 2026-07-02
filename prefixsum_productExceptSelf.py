class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suff=[0]*len(nums)
        suff[-1]=1
        pref=[0]*len(nums)
        pref[0]=1
        
        for i in range(len(nums)-2,-1,-1):
            suff[i]=nums[i+1]*suff[i+1]
        
        for i in range(1,len(nums)):
            pref[i]=nums[i-1]*pref[i-1]
        r=[0]*len(nums)
        for i in range(len(nums)):
            r[i]=suff[i]*pref[i]
        return r
