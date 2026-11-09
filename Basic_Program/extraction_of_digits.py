n = 5873
count = 0
num = n

while(num > 0):
    last_digit = num % 10
    print(last_digit)
    num = num // 10

print(count)