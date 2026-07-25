class Solution:
	def prevSmaller(self, arr):
		# code here
		st=[]
		arr2=[]
		for i in range(len(arr)):
		    if st==[]:
		        arr2.append(-1)
		    elif arr[i]>st[-1]:
		        arr2.append(st[-1] )
		    elif arr[i]<=st[-1]:
		        while st!=[] and arr[i]<=st[-1]:
		            st.pop()
		        if st==[]:
		            arr2.append(-1)
		        else:
		            arr2.append(st[-1])
		    st.append(arr[i])
        return arr2
