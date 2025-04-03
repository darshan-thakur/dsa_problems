from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        registry = defaultdict(int)
        for num in nums:
            registry[num]+=1
        
        approach = 3 #unrelated to the problem, but just to choose the approach in execution

        if approach == 1:
            #Approach 1: Using sorting
            ans = list(sorted(registry.keys(), key=lambda x:registry[x]))
            return ans[-k:]

        elif approach == 2:
            # Approach 2: Using heap
            import heapq
            new_list = [(0-v,k) for k,v in registry.items()]
            heapq.heapify(new_list)
            topk = []
            for i in range(k):
                topk.append(heapq.heappop(new_list)[1])
            return topk

        else:
            #Approach 3: Using bucket sort
            bucket_list = [[] for _ in range(len(nums)+1)]
            for key,val in registry.items():
                bucket_list[val].append(key)
            topk = []
            for numlist in bucket_list[::-1]:
                for num in numlist:
                    topk.append(num)
                    k-=1
                    if k == 0:
                        return topk
            

obj = Solution()    
print(obj.topKFrequent([1,1,1,2,2,3], 2))


        