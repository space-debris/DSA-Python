def isPalindrome(s: str) -> bool:
    def plnd(s,i):
        n=len(s)
        if i>=n/2:
            return True
        if s[i] != s[n-i-1]:
            return False
        return plnd(s,i+1)
    return plnd(s,0)

s ="A man, a plan, a canal: Panama"   
new_s=''.join([char for char in s if char.isalnum()]).lower()     
print(isPalindrome(new_s))
    