class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr=[]
        arr2=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum1=nums1[i]+nums2[j]
                if len(arr)<k:
                    heapq.heappush(arr,(-sum1,[nums1[i],nums2[j]]))
                elif sum1<-1*arr[0][0]:
                    heapq.heappop(arr)
                    heapq.heappush(arr,(-sum1,[nums1[i],nums2[j]]))
                else:
                    break
        for i in range(k):
            arr2.append(heapq.heappop(arr)[1])
        return arr2
