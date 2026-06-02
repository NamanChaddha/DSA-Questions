class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        s=[]
        for i in range(len(l)):
            c=0
            k=nums[l[i]:r[i]+1]
            k.sort()
            if len(k)==2:
                s.append(True)
            else:
                for j in range(len(k)-2):
                    if (k[j]-k[j+1])!=(k[j+1]-k[j+2]):
                        c=1
                        break
                    else:
                        continue
                if c==0:
                    s.append(True)
                else:
                    s.append(False)
        return s
