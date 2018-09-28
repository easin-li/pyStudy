# -*- coding: UTF-8 -*-
# 列表生成式 列表生成器里面可以用函数 yield
def f(n):
    return n * n

print([f(x) for x in range(10)])

# 列表 元组等可以一次性取出赋值  a ,b , c = (1,2,3)  此时 a b c 三个值分别等于 1 2 3