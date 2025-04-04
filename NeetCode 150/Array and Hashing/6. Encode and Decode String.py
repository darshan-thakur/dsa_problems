from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word))+ "#" + word
        return output
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        output = []
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            output.append(s[j+1:j+length+1])
            i = j+length+1
            
        return output


obj = Solution()
input = ["we","say",":","yes","!@#$%^&*()"]
enc = obj.encode(input)
dec = obj.decode(enc)
print(input==dec) #True
