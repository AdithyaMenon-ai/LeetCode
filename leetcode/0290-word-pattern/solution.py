class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        s1 = s.split()

        if len(pattern) != len(s1):
            return False

        for i in range(len(s1)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != s1[i]:
                    return False
            else:
                if s1[i] in mapping.values():
                    return False
                mapping[pattern[i]] = s1[i]

        return True
