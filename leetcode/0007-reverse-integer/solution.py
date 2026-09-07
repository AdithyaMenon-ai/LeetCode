
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 or +1 if x < 0 else 1
        x = abs(x)

        for i in str(x):
            if i.isdigit():
                rem = x % 10
                rev = rev * 10 + rem
                x = x // 10

        rev = rev * sign

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev


