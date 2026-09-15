class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]

        return True
