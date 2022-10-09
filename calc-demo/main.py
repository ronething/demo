# coding=utf-8
# 简单公式计算
import sys
from math import sqrt


def calc_sample(a: int, b: int):
    c = (a * 10 ** 6) / (14.3 * 1000 * b ** 2)
    c = format(c, ".3f")
    print("(a * 10^6) / (14.3 * 1000 * b^2) = ", c)
    d = 1 - sqrt(1 - 2 * float(c))
    d = format(d, ".3f")
    print("1 - sqrt(1 - 2 * c) = ", d)
    e = 1 - 0.5 * float(d)
    e = format(e, ".3f")
    print("1 - 0.5 * d = ", e)
    f = (a * 10 ** 6) / (360 * float(e) * b)
    f = "%.0f" % f
    print("(a * 10^6) / (360 * e * b) = ", f)


if __name__ == "__main__":
    # input a b
    # calc(a=2.5, b=60)
    try:
        # print(sys.argv)
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except:
        print("输入错误，需要两个参数 a and b")
        sys.exit(1)
    calc_sample(a, b)
