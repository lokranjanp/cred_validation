# luhn.py
import random


def digits_of(n):
    return [int(d) for d in str(n)]


def luhn_check(num):
    digits = digits_of(num)
    checksum = 0
    is_second = False
    for d in reversed(digits):
        if is_second:
            d = d * 2
            if d > 9:
                d = d - 9
        checksum += d
        is_second = not is_second
    return checksum % 10 == 0


def generate_luhn_number(prefix, length):
    num = [int(x) for x in str(prefix)]
    while len(num) < (length - 1):
        num.append(random.randint(0, 9))
    checksum = 0
    is_second = True
    for d in reversed(num):
        if is_second:
            d = d * 2
            if d > 9:
                d = d - 9
        checksum += d
        is_second = not is_second
    check_digit = (10 - (checksum % 10)) % 10
    num.append(check_digit)
    return ''.join(map(str, num))
