class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        value=''
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i,x in dic.items():
            if x==1:
                value+=i
                break
        else:
            return -1
        return s.index(value)
