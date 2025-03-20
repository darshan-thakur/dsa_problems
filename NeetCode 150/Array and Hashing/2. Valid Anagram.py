from collections import defaultdict

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
    
    def isAnagram2(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in range(max(len(s),len(t))):
            if i < len(s):
                s_count[s[i]]+=1
            if i < len(t):
                t_count[t[i]]+=1
        for char in s_count:
            if s_count[char] != t_count[char]:
                return False
        for char in t_count:
            if s_count[char] != t_count[char]:
                return False
        return True
    
    from collections import defaultdict

    def isAnagram3(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in range(max(len(s),len(t))):
            if i < len(s):
                count[s[i]]+=1
            if i < len(t):
                count[t[i]]-=1
        for char in count:
            if count[char] != 0:
                return False
        return True

    def isAnagram4(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in range(max(len(s),len(t))):
            if i < len(s):
                count[s[i]]+=1
            if i < len(t):
                count[t[i]]-=1
        if any(count.values()):
            return False
        else:
            return True
        
obj = Solution()
print(obj.isAnagram1("racecar","carrace"))
print(obj.isAnagram2("racecar","carrace"))
print(obj.isAnagram3("racecar","carrace"))
print(obj.isAnagram4("racecar","carrace"))

        
        