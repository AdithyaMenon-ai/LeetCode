class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ca=max(candies)
        result=[]

        for i in candies:
            if max_ca <= i + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result

        
