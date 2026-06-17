class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[]
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                arr.append(nums[i])
            else:
                d[nums[i]]=1
        return arr
        
