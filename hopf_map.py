import math
import sys


def get_x(a, b, c, d):
    return a ** 2 + b ** 2 - c ** 2 - d ** 2


def get_y(a, b, c, d):
    return 2 * (a * d + b * c)


def get_z(a, b, c, d):
    return 2 * (b * d - a * c)


def adds_to_one(a, b, c, d):
    return round(a ** 2 + b ** 2 + c ** 2 + d ** 2) == 1


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


def main():
    """You will have to either modify the run configuration or run the code through the
    terminal to enter values. """
    numbers = sys.argv[1:]
    nums = []

    # turns the numbers into floats
    for num in numbers:
        if is_fraction(num):
            num = convert_frac(num)
            nums.append(num)
        elif is_sqrt(num):
            num = convert_sqrt(num)
            nums.append(num)
        else:
            nums.append(num)

    a, b, c, d = float(nums[0]), float(nums[1]), float(nums[2]), float(nums[3])

    # maps points to corresponding coordinates
    if adds_to_one(a, b, c, d):
        x = get_x(a, b, c, d)
        y = get_y(a, b, c, d)
        z = get_z(a, b, c, d)

        # prints information
        point_1 = f"{(a, b, c, d)}"
        point_2 = f"({round(x, 5)},{round(y, 5)},{round(z, 5)})"
        print(f"The coordinates on the 3-sphere squared sum to {a ** 2 + b ** 2 + c ** 2 + d ** 2}")
        print(f"{point_1} -> {point_2}.")
        print(f"The coordinates on the 2-sphere squared sum to {x ** 2 + y ** 2 + z ** 2}.")
    else:
        print("a^2 + b^2 + c^2 + d^2 does not equal 1")


if __name__ == '__main__':
    main()
