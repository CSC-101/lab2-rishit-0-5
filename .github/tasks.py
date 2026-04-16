def smallest(n:float,m:float) -> float:
    if n<m:
        return n        #This statement is evaluated for the second call
    else:
        return m

first=smallest(3,2)         #first=2
second=smallest(2,2)        #second=2, It's not a reasonable result because neither value is smaller, but it returns m anyways
print(first)
print(second)

def function2(a:int,b:int,c:int) -> float:
    if a>b and a>c:
        return a-b      #this statement will be evaluated when a>b and a>c
    elif b>c:
        return b+c      #this statement will be evaluated when b>c and a<b or a<c
    else:
        return 2*c      #this statement will be evaluated when b<=c, and a<b or a<c
answer1=function2(3,2,1)        #answer1=1
answer2=function2(2,3,1)        #answer2=4
answer3=function2(2,1,3)        #answer3=6
print(answer1)
print(answer2)
print(answer3)
