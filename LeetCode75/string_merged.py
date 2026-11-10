def mergeAlternately(word1, word2):

        i = 0
        j = 0
        n = len(word1)-1
        m = len(word2)-1
        merged = ''

        while i <= n and j <= m:
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        
        while i <= n:
            merged += word1[i]
            i += 1
            
        while j <= m:
            merged += word2[j]
            j += 1

        return merged


             

word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1,word2))


