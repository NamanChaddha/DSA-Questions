class Solution:
    
    def minElement(self, nums: List[int]) -> int:
        def sumofdigits(self,num):
            for i in range(len(nums)):
                c=0
                while nums[i]!=0:
                    c+=nums[i]%10
                    nums[i]=nums[i]//10
                nums[i]=c
            print(nums)
            return nums
        return min(sumofdigits(self,nums))
