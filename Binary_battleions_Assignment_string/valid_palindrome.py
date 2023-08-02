class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=''.join(i.lower() for i in s if i.isalnum())
        res=n[::-1]
        return n==res