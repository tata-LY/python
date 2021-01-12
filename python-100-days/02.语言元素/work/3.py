# 输入年份判断是不是闰年。
# 闰年提示：能被4整除但是不能被100整除，或者可以直接被400整除
year = int(input("输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d年是闰年。" % year)
else:
    print("%d年不是闰年" % year)