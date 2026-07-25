class Solution:
	def nextSmallerEle(self, arr):
		# code here
		st=[]
		arr2=[]
		for i in range(len(arr)-1,-1,-1):
		    if st==[]:
		        arr2.append(-1)
		    elif arr[i]>st[-1]:
		        arr2.append(st[-1])
		    elif arr[i]<=st[-1]:
		        while st!=[] and st[-1]>=arr[i]:
		            st.pop()
		        if st!=[]:
		            arr2.append(st[-1])
		        else:
		            arr2.append(-1)
		    st.append(arr[i])
	    return arr2[::-1]
	#redused time complexity tpo o(n)(naman's way ))
