def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # This statement is evaluated for either call
    else:
        return m

first = smallest(3, 2)       # first=2
second = smallest(2, 2)      # second=2, which is reasonable since there's no way for the code to differentiate identical values
print()


def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement?
    elif b > c:
        return b + c             # In general, when will a call to this function evaluate this statement?
    else:
        return 2 * c             # In general, when will a call to this function evaluate this statement?


answer1 = function2(3, 2, 1)     # What is the value of answer1?
answer2 = function2(2, 3, 1)     # What is the value of answer2?
answer3 = function2(2, 1, 3)     # What is the value of answer3?
print()