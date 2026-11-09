## Infinite Recursion
# def greet():
#     print("Greeting !")
#     greet()

# greet()

## Print "jay" 4 times using recurion
# count = 0
# def namePrint():
#     global count
#     if count == 4:
#         return 
#     print("Jay")
#     count +=1
#     namePrint()
# namePrint()

## Recursion using Parameters

# def func(X,N):
#     if N == 0:
#         return 
#     func(X,N-1)
#     print(X)
# func(15,4)

## 1 to N using Tail
def func(N):
    if N == 0:
        return
    func(N-1)
    print(N)
func(4)