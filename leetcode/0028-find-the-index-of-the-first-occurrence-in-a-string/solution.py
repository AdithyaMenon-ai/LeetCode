class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the first occurrence of needle in haystack.
      
        Args:
            haystack: The string to search in
            needle: The substring to search for
          
        Returns:
            The index of the first occurrence of needle in haystack,
            or -1 if needle is not found
        """
        # Get lengths of both strings
        haystack_length = len(haystack)
        needle_length = len(needle)
      
        # Iterate through all possible starting positions in haystack
        # We only need to check positions where there's enough space for needle
        for start_index in range(haystack_length - needle_length + 1):
            # Check if substring starting at current position matches needle
            if haystack[start_index:start_index + needle_length] == needle:
                # Found a match, return the starting index
                return start_index
      
        # No match found in the entire haystack
        return -1
