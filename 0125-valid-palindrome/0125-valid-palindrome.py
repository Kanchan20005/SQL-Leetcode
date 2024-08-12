class Solution:
    def isPalindrome(self, s: str) -> bool:
        split_string = [char.lower() for char in s if char.isalnum()]
        if len(split_string) ==0 or len(split_string) ==1:
            return True
        siz = len(split_string)
        first = split_string[0]
        last = split_string[siz-1]
        for i in range(int(len(split_string)/2)):
            if first != last:
                return False
            first = split_string[i+1]
            last =split_string[siz-2-i]
        return True