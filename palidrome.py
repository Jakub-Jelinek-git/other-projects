def isPalindrome(x):
        
        x = str(x)[::-1]==str(x)
        return x

print(isPalindrome(12))