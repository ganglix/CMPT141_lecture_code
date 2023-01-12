# bonus example: integer division
# header
# actions

"""
Algorithm: integer division
input: dividend, divisor
output: integer quotient = dividend/ divisor

remainder = dividend - divisor
check if remainder >0.
if so, keep subtracting divisor from  remainder,
    repeat the subtraction until remainder <0
count how many of divisors have been subtracted
quotient = number of subtracted divisors -1

"""
# you don't have to fully understand the code. Just appreciate how readable it is (almost like pseudocode)
def int_divisor(dividend, divisor):
    remainder = dividend - divisor
    count = 1
    while remainder > 0:
        remainder = remainder - divisor
        count = count + 1
    return count - 1

print( int_divisor(1, 3))

