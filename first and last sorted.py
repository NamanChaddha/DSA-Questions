class Solution(object):
    def searchRange(self, nums, target):
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==target:
                if nums[j]==target:
                    return [i,j]
                else:
                    j-=1
            elif nums[i]!=target:
                if nums[j]==target:
                    i+=1
                else:
                    i+=1
                    j-=1
        return [-1,-1]


        