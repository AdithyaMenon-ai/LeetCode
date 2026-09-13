class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro=0
        min_pri = prices[0]

        for i in prices:
            if i<min_pri:
                min_pri=i
            pro = i-min_pri

            max_pro = max(max_pro,pro)


        return max_pro
