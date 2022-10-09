# coding=utf-8

# 简单生成器
def simple_gen():
    yield 'hello'
    yield 'world'


if __name__ == '__main__':
    gen = simple_gen()
    print(type(gen))  # <class 'generator'>
    print(next(gen))  # hello
    print(next(gen))  # world
