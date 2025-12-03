class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end of the string
        end_index = len(s) - 1
      
        # Skip trailing spaces from the end
        while end_index >= 0 and s[end_index] == ' ':
            end_index -= 1
      
        # Mark the end position of the last word
        last_word_end = end_index
      
        # Find the beginning of the last word by moving backwards
        # until we hit a space or reach the start of the string
        start_index = last_word_end
        while start_index >= 0 and s[start_index] != ' ':
            start_index -= 1
      
        # Calculate the length of the last word
        # start_index points to the space before the word (or -1 if at beginning)
        # so the length is the difference between end and start positions
        return last_word_end - start_index
