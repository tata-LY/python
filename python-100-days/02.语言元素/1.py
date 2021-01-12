# 使用变量保存数据并进行+-*/
a = 123
b = 321
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 使用type检查变量类型
a = 100
b = 100.00
c = 100+5j
d = '100'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 装换
print(type(int(d)))
print(float(a))

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))