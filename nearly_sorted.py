import heapq

class Solution:
    def nearlySorted(self, arr, k):
        minheap = []

        for i in range(min(k + 1, len(arr))):
            heapq.heappush(minheap, arr[i])

        index = 0

        for i in range(k + 1, len(arr)):
            arr[index] = heapq.heappop(minheap)
            heapq.heappush(minheap, arr[i])
            index += 1

        while minheap:
            arr[index] = heapq.heappop(minheap)
            index += 1

        return arr
