nums = []
def largest_prime_factor(num, div=2):
    while div < num:
        if num % div == 0 and num/div > 1:
            num = num /div
            div = 2
        else:
            div = div + 1
    return num

print largest_prime_factor(600851475143)
