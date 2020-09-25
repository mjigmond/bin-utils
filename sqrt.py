# -*- coding: utf-8 -*-
import math
import random


def user_sqrt(num: float, decimals: int) -> str:
    """
    Calculate the square root of a number. Beyond a certain number of decimals
    it will no longer match the `math.sqrt(x)` which is less precise.

    Parameters
    ----------
    num : float
        Number whose square root we need to find.
    decimals : int
        How many decimals should the result have.

    Returns
    -------
    str
        Square root of `num`.

    """
    if num <= 0:
        return '0'

    e = 3

    fmtd_num = f'{num:.{decimals*2+e}f}'[:-e]

    left, right = fmtd_num.split('.')

    left = left[-1::-1]
    left_list = [left[i:i+2][-1::-1] for i in range(0, len(left), 2)]
    left_list.reverse()

    right_list = [right[i:i+2] for i in range(0, len(right), 2)]

    g = 1
    n = int(left_list[0])
    while g**2 <= n:
        g += 1
    lo = n - (g - 1)**2

    res = str(g - 1)
    for n in left_list[1:] + right_list:
        lo = int(str(lo) + n)
        t = int(res) * 2 * 10
        i = 0
        while (t + i) * i <= lo:
            i += 1
        lo = lo - (t + i - 1) * max(0, i - 1)
        res += str(max(0, i - 1))

    sqrt = res[:len(left_list)] + '.' + res[len(left_list):]
    return sqrt


if __name__ == '__main__':
    for i in range(100):
        num = random.uniform(0, 1e7)
        dec = random.randint(0, 9)

        math_sqrt = math.sqrt(num)
        math_sqrt = f'{math_sqrt:.{dec+5}f}'[:-5]

        sqrt = user_sqrt(num, dec)
        # print(f'The square root of {num}, up to {dec} decimals is: {sqrt}')
        assert  sqrt == math_sqrt, f'The square root of {num}, up to {dec} decimals is: {sqrt} vs {math_sqrt}'
