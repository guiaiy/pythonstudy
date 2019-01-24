# 导入模块时，代码将会执行一遍
from day03 import randpass
from day03 import star

print(star)
print(star.pstar(20))

# 每个模块都有一个变量__name__,直接执行返回__main__,导入返回模块名


print(randpass.getpass(8))
