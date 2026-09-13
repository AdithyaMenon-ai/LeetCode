class Solution:
    def isPalindrome(self, s: str) -> bool:
        ts=''
        while True:
            for i in s:
                if i.isalnum():
                    ts+=i.lower()
            return ts==ts[::-1]
        
