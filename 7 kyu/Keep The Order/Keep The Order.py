```py
def keep_order(ary, val):
    i = 0
    while i < len(ary):
        if ary[i] >= val:
            break
        i += 1
    return i
print(keep_order([1, 2, 3, 4, 7], 5))
print(keep_order([1, 2, 3, 4, 7], 0))
print(keep_order([1, 1, 2, 2, 2], 2))
```py
