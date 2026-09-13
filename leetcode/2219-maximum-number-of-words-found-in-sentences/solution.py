class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_co=0
        for i in sentences:
            curr_co = len(str(i).split(' '))

            if max_co<curr_co:
                max_co=curr_co
        return max_co

    

        
