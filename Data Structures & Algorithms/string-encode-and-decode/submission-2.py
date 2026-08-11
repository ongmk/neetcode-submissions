class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += f"{len(string)}#{string}"
        
        return out
        

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0

        out = []
        while right < len(s):
            if s[right] == "#":
                length = int(s[left:right])
                string = s[right+1:right+length+1]
                out.append(string)
                left = right = right+length+1
            else:
                right += 1
        
        return out