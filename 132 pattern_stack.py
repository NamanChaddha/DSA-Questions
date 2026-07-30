class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        st=[]
        mx=float('-inf')
        for i in range(n-1,-1,-1):
            if(nums[i]<mx):
                return True
            while len(st)!=0 and nums[i]>st[-1]:
                mx=st[-1]
                st.pop()
            st.append(nums[i])
        return False
        
                
