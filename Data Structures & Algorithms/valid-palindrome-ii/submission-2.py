import re

class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_altered = ""

        for char_index in range(len(s)):
            s_altered = s[:char_index:] + s[char_index + 1::]
            s_altered = re.sub(r'[^a-zA-Z0-9]','', s_altered).lower()
            if s_altered == "".join(reversed(s_altered)):
                return True

        return False
