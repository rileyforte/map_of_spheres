import math
import sys

"""This one does not output coordinates that square to 1. Still working 
on it. """


def get_a2(a, b, c, d, t, s):
    return (a ** 2 + b ** 2 - c ** 2 - d ** 2) * (math.sqrt(1 - t ** 2)) * (math.sqrt(1 - s ** 2))


def get_b2(a, b, c, d, t, s):
    return (2 * (a * d + b * c)) * (math.sqrt(1 - t ** 2)) * (math.sqrt(1 - s ** 2))


def get_c2(a, b, c, d, t, s):
    return (2 * (b * d - a * c)) * (math.sqrt(1 - t ** 2)) * (math.sqrt(1 - s ** 2))


def get_d2(a, b, c, d, t, s):
    return t * (math.sqrt(1 - s ** 2))


def get_e2(a, b, c, d, t, s):
    return s


def adds_to_one(a, b, c, d, t, s):
    sum = a ** 2 + b ** 2 + c ** 2 + d ** 2 + t ** 2 + s ** 2
    print(f"The input coordinates squared sum to {sum}.")
    return sum


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


def summed_cords(a2, b2, c2, d2, e2):
    return a2 ** 2 + b2 ** 2 + c2 ** 2 + d2 ** 2 + e2 ** 2


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

    a, b, c, d, t, s = float(nums[0]), float(nums[1]), float(nums[2]), float(nums[3]), float(nums[4]), float(nums[5])

    if adds_to_one(a, b, c, d, t, s):
        a2 = get_a2(a, b, c, d, t, s)
        b2 = get_b2(a, b, c, d, t, s)
        c2 = get_c2(a, b, c, d, t, s)
        d2 = get_d2(a, b, c, d, t, s)
        e2 = get_e2(a, b, c, d, t, s)
        vector_magnitude = math.sqrt(summed_cords(a2, b2, c2, d2, e2))
        a2 = get_a2(a, b, c, d, t, s) / vector_magnitude
        b2 = get_b2(a, b, c, d, t, s) / vector_magnitude
        c2 = get_c2(a, b, c, d, t, s) / vector_magnitude
        d2 = get_d2(a, b, c, d, t, s) / vector_magnitude
        e2 = get_e2(a, b, c, d, t, s) / vector_magnitude
        point_1 = f"({round(a, 5)}, {round(b, 5)}, {round(c, 5)}, {round(d, 5)}, {round(t, 5)}, {round(s, 5)})"
        point_2 = f"({round(a2, 5)}, {round(b2, 5)}, {round(c2, 5)}, {round(d2, 5)}, {round(e2, 5)})"
        print(f"The point {point_1} maps to {point_2}.")
        print(f"The output coordinates squared sum to {summed_cords(a2, b2, c2, d2, e2)}.")
    else:
        print("a^2 + b^2 + c^2 + d^2 + t^2 + s^2 does not equal 1")


if __name__ == '__main__':
    main()
