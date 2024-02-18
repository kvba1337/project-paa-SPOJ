# zrodla z ktorych czerpalem wiedze dotyczaca prezycji wyniku:
# https://docs.python.org/3/tutorial/floatingpoint.html
# https://en.wikipedia.org/wiki/Floating-point_arithmetic
# https://stackoverflow.com/questions/8362792/how-do-i-shift-the-decimal-place-in-python
# https://realpython.com/python-rounding/

from math import isqrt

DOUBLE = 2

def calculate_roots(a, b, c, k, shift):
    if a == 0:
        return calculate_linear_roots(b, c, k, shift)
    else: 
        if a < 0:
            a, b, c = -a, -b, -c
        return calculate_quadratic_roots(a, b, c, k, shift)

def calculate_linear_roots(b, c, k, shift):
    if b == 0:
        return "1 0" if c== 0 else "0"
    else:
        sign = "-" if (b > 0 and c > 0) or (b < 0 and c < 0) else ""
        b_abs, c_abs = abs(b), abs(c)
        result_scaled = (shift * c_abs) // b_abs
        result_fraction = result_scaled % shift
        result_int = result_scaled // shift
        result_formated_dec = str(result_fraction).zfill(k)
        return f"1 {sign}{result_int}.{result_formated_dec}"

def calculate_quadratic_roots(a, b, c, k, shift):
    delta = b * b - 4 * a * c

    if delta < 0:
        return "0"
    elif delta == 0:
        return calculate_single_root(a, b, k, shift)
    else:
        return calculate_complex_roots(a, b, k, delta, shift)

def calculate_single_root(a, b, k, shift):
    numerator = abs(b)
    denominator = DOUBLE * a
    result_scaled = (shift * numerator) // denominator
    result_fraction = result_scaled % shift
    result_int = result_scaled // shift
    result_formated_dec = str(result_fraction).zfill(k)
    sign = "-" if b > 0 else ""
    return f"1 {sign}{result_int}.{result_formated_dec}"

def calculate_complex_roots(a, b, k, delta, shift):
    square_root_delta = isqrt(shift * shift * delta)
    numerator1 = -b * shift - square_root_delta
    numerator2 = -b * shift + square_root_delta
    denominator = DOUBLE * a
    return (
        f"2 {calculate_root_part(numerator1, denominator, shift, k)}" +
        f" {calculate_root_part(numerator2, denominator, shift, k)}"
    )

def calculate_root_part(numerator, denominator, shift, k):
    if numerator < 0:
        sign = "-" 
        numerator = abs(numerator)
    else:
        sign = ""
    result_scaled = numerator // denominator
    result_fraction = result_scaled % shift
    result_int = result_scaled // shift
    result_formated_dec = str(result_fraction).zfill(k)
    return f"{sign}{result_int}.{result_formated_dec}"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, k = [int(x) for x in input().split()]
        shift = 10 ** k
        roots = calculate_roots(a, b, c, k, shift)
        print(roots)