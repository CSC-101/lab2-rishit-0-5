from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # first: False, second=True
    if test:                            # That the list isn't indexed for an entry that it doesn't have
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # first=none
second = checked_access([1, 0, 1], 2)    # second=1
print()


def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # This statement is evaluated for just the first call
    elif len(L) > 1:                                  # 4+2+3=9
        result = len(L[0]) + len(L[1])                # This statement is evaluated for the third call
    elif len(L) > 0:                                  # 7+4=11
        result = len(L[0])                            # This statement is evaluated for the second call
    else:                                             # 11=11
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # words=['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
         # first=['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.'], second=['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
         # Since each function call modified the list, function call first, function call second, and words all equal the same modified list
print()