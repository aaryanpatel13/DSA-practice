def palindromeString(word,i):
    n = len(word)
    if i >= n//2:
        return True
    if word[i] != word[n-i-1]:
        return False
    return palindromeString(word, i+1)

s = 'MADAM'
print(palindromeString(s,0))