# s = "nitin"
# left = 0
# right = len(s) - 1
# a = True
# while(left < right):
#                 if s[left] != s[right]:
#                     a = False
#                 left += 1
#                 right -= 1

# if a == True:
#        print("Palindrome")
# else:
#       print("Not Palindrome")




def revStr(s,left,right):
        if left >= right:
            return True
        if s[left] != s[right]:
              return False
        return revStr(s,left+1,right-1)

s = "nitin"
left = 0
right = len(s) - 1
print(revStr(s,left,right))