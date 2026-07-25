class Solution:
	def preGreaterEle(self, arr):
		# code here
		st=[arr[0]]
		arr2=[]
		for i in range(len(arr)):
		    if len(st)==0:
		        arr.append(-1)
		    if arr[i]<st[-1]:
		        arr2.append(st[-1])
		    elif arr[i]>=st[-1]:
		        while st!=[] and st[-1]<=arr[i]:
		            st.pop()
		        if st!=[]:
		            arr2.append(st[-1])
		        else:
		            arr2.append(-1)
            st.append(arr[i])
		return arr2  
