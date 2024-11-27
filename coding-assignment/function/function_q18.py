# function to calculate digital root of a number
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Test
print(digital_root(9875))  # 2 (9+8+7+5=29 -> 2+9=11 -> 1+1=2)
