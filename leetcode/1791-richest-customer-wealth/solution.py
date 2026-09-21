class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for i in accounts:
            wealth=sum(i)
            if wealth>maximum:
                maximum=sum(i)
        return maximum        
