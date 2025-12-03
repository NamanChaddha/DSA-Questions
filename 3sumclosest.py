class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        cl=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                curr=nums[i]+nums[j]+nums[k]
                if abs(curr-target)<abs(cl-target):
                    cl=curr
                if curr==target:
                    return curr
                elif curr<target:
                    j+=1
                else:
                    k-=1
        return cl