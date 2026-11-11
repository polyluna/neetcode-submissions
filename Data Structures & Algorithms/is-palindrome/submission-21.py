class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char for char in s if char.isalnum())
        print(cleaned_s)
        
        if (len(cleaned_s)) % 2 == 0:
            mid = (len(cleaned_s))//2
            s1 = cleaned_s[:mid].lower()
            s2 = cleaned_s[mid::].lower()
            s2 = s2[::-1]

        else:
            mid = (len(cleaned_s))//2
            s1 = cleaned_s[:mid].lower()
            s2 = cleaned_s[mid+1::].lower()
            s2 = s2[::-1]
        

        return s1 == s2
            