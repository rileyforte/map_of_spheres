import math
import sys


def get_a2(a, b, c, d, t):
    return (a ** 2 + b ** 2 - c ** 2 - d ** 2) * (math.sqrt(1 - t ** 2))


def get_b2(a, b, c, d, t):
    return (2 * (a * d + b * c)) * (math.sqrt(1 - t ** 2))


def get_c2(a, b, c, d, t):
    return (2 * (b * d - a * c)) * (math.sqrt(1 - t ** 2))


def get_d2(a, b, c, d, t):
    return t


def adds_to_one(a, b, c, d, t):
    print(f"The coordinates on the 4-sphere squared sum to {a ** 2 + b ** 2 + c ** 2 + d ** 2 + t ** 2}.")
    return round(a ** 2 + b ** 2 + c ** 2 + d ** 2 + t ** 2) == 1


def is_fraction(num):
    return '/' in num


def convert_sqrt(num):
    nums = num.split('(')
    nums = nums[1].split(')')
    num = int(nums[0])
    return math.sqrt(num)


def convert_frac(num):
    num = num.split('/')
    if is_sqrt(num[0]):
        numerator = convert_sqrt(num[0])
    else:
        numerator = float(num[0])
    if is_sqrt(num[-1]):
        denominator = convert_sqrt(num[-1])
    else:
        denominator = float(num[-1])
    return numerator / denominator


def is_sqrt(num):
    return 'sqrt' in num


def summed_cords(a2, b2, c2, d2):
    return a2 ** 2 + b2 ** 2 + c2 ** 2 + d2 ** 2


def main():
    numbers = sys.argv[1:]
    nums = []

    for num in numbers:
        if is_fraction(num):
            num = convert_frac(num)
            nums.append(num)
        elif is_sqrt(num):
            num = convert_sqrt(num)
            nums.append(num)
        else:
            nums.append(num)

    a, b, c, d, t = float(nums[0]), float(nums[1]), float(nums[2]), float(nums[3]), float(nums[4])

    if adds_to_one(a, b, c, d, t):
        a2 = get_a2(a, b, c, d, t)
        b2 = get_b2(a, b, c, d, t)
        c2 = get_c2(a, b, c, d, t)
        d2 = get_d2(a, b, c, d, t)
        point = f"({round(a2, 5)},{round(b2, 5)},{round(c2, 5)},{round(d2, 5)})"
        print(point)
        print(f"The coordinates on the 3-sphere squared sum to {summed_cords(a2, b2, c2, d2)}.")
    else:
        print("a^2 + b^2 + c^2 + d^2 + t^2 does not equal 1")


if __name__ == '__main__':
    main()
    
