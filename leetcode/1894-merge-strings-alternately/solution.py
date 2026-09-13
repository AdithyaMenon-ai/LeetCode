class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        wo1=0
        wo2=0
        while wo1<len(word1) or wo2<len(word2):
            if len(word1)>wo1:
                res+=word1[wo1]
                wo1+=1
            if len(word2)>wo2:
                res+=word2[wo2]
                wo2+=1

        return res
