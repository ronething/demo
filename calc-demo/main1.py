# coding=utf-8
# 简单公式计算
import sys
from math import sqrt


def calc_sample(m: int, b: int, h: int):
    a_s = (m * 10 ** 6) / (14.3 * b * h ** 2)
    a_s = format(a_s, ".3f")
    e = 1 - sqrt(1 - 2 * float(a_s))
    e = format(e, ".3f")
    A_s = float(e) * b * h * 14.3 / 360
    A_s = format(A_s, ".3f")
    p = float(A_s) / (b * h)
    p = format(p, ".4f")
    v1 = 0.25 * 14.3 * b * h
    v1 = format(v1, ".3f")
    v2 = 0.7 * 1.43 * b * h
    v2 = format(v2, ".3f")
    print("as = ",a_s)
    print("e = ",e)
    print("As = ", A_s)
    print("p = ", p)
    print("v1 = ", v1)
    print("v2 = ", v2)


if __name__ == "__main__":
    # input a b
    # calc(a=2.5, b=60)
    try:
        # print(sys.argv)
        m = float(sys.argv[1])
        b = float(sys.argv[2])
        h = float(sys.argv[3])
    except:
        print("输入错误，需要三个参数 m, b and h")
        sys.exit(1)
    calc_sample(m, b, h)
