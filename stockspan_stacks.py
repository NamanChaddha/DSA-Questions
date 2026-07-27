class Solution:
    def calculateSpan(self, arr):
        # code here
        st=[]
        arr2=[]

        for i in range(len(arr)):
            if st==[]:
                arr2.append(1)
            elif arr[i]<st[-1][1]:
                arr2.append(i-st[-1][0])
            else:
                while st!=[] and st[-1][1]<=arr[i]:
                    st.pop()
                if st==[]:
                    arr2.append(i+1)
                else:
                    arr2.append(i-st[-1][0])
            st.append((i,arr[i]))
        return arr2
