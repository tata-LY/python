#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

def test(num=0):
    result = num * 2
    return result


generator1 = (test(i) for i in range(10))
print(generator1)

# for i in generator1:
#     print(i)
# 取完后后面就取不到了

print(generator1.__next__())
print(generator1.__next__())
print(generator1.__next__())


# 斐波那契
print("斐波那契：")
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1

fib(10)

# 斐波那契生成器
print("斐波那契生成器：")
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"

print(fib(10))
fib_gen = fib(10)
# print(fib_gen.__next__())
# print(fib_gen.__next__())
# print(fib_gen.__next__())
# print(fib_gen.__next__())

# print("start loop: ")
# for i in fib_gen:
#     print(i)

while True:
    try:
        x = next(fib_gen)
        print("fib_gen: ", x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break

data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]
print("before sort:", data)

previous = data[0]
for j in range(len(data)):
    tmp = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
    print(data)

print("after sort:", data)