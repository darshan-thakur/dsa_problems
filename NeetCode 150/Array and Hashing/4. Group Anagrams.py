from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabets = [0]*26
        registry = defaultdict(list)
        for word in strs:
            temp_alphabets = alphabets.copy()
            for letter in word:
                temp_alphabets[ord(letter)-ord("a")]+=1
            registry[tuple(temp_alphabets)].append(word)

        return list(registry.values())


obj = Solution()    
print(obj.groupAnagrams(["racecar","carrace","den","end","for","of"]))