class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        k=0
        m=len(nums)-1
        arr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                m=len(nums)-1
                while k<m:
                    if nums[i]+nums[j]+nums[k]+nums[m]==target:
                        if [nums[i],nums[j],nums[k],nums[m]] not in arr:
                            arr.append([nums[i],nums[j],nums[k],nums[m]])
                        k+=1
                        m-=1
                    elif (nums[i]+nums[j]+nums[k]+nums[m])>target:
                        m-=1
                    else:
                        k+=1
        return arr