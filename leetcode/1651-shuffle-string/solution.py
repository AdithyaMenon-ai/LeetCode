class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=0
        result=[' ']* len(s)
        for i in range (len(indices)):
            result[indices[i]]=s[x]
            x+=1
        return ''.join(result)

        
