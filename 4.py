def is_palindromic(n):
    digits = str(n)
    num_digits = len(digits)
    for i in range(0, int(num_digits / 2)):
        if digits[i] != digits[num_digits - 1 - i]:
            return False
    return True


def largets_palindromic_num(n):
    largest_num = 0
    for i in range(pow(10, n), 0, -1):
        for j in range(pow(10, n)):
            num = i * j
            if is_palindromic(num):
                if num > largest_num:
                    largest_num = num
    return largest_num


print(largets_palindromic_num(3))
