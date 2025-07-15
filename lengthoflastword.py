class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        words = s.split()  # Split into list of words
        return len(words[-1])  # Return length of last word
