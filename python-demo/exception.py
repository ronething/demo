# coding=utf-8
import time


class MyException(Exception):
    pass


def func():
    print("hello")
    # raise MyException("occur exception")


def main():
    try:
        func()  # 可能会有抛出异常的代码
        time.sleep(10)
    except Exception as e:  # 可以捕获多个异常
        print(e, type(e))  # 处理异常的代码
    else:  # 没有发生异常的时候会执行的代码逻辑
        pass
    finally:  # 无论异常有没有发生，最后都会进行代码的执行，一般可以用于处理资源的关闭和释放
        pass


if __name__ == '__main__':
    main()
