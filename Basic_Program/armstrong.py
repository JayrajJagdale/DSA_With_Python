n = 153
num = n
sums = 0
count = 0

while(num > 0):
    count += 1
    ld = num % 10
    num = num // 10

num = n
while(num > 0):
        ld = num % 10
        sums += ld ** count
        num = num // 10
print(sums)
        



    
