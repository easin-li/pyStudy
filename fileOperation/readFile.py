# -*- coding: UTF-8 -*-
# 如果制定了当前编码为utf8 编码，则该文件中的汉字都是byte string格式。
# 在函数中取数来的字符串一般是unicode string格式
# 文件操作的步骤：打开文件-操作文件-关闭文件
import io

# 读取文件的两种方法
# 1, 拿到文件描述器，将文件加入到内存中，适合小文件 f.readLines(),在生产环境中尽量少用readLines()方法
f = io.open("onePoem", "r", encoding="utf-8")
for i in f.readlines():
    print(i.strip())

# 2,拿到文件描述器，然后获取文件迭代器,此时在读取的时候会利用迭代器一部分一部分读取文件，对于大文件也不会太消耗内存
for j in f:
    print(j.strip())

# s = u"你好"
# print(s)
# s2 = s.encode("UTF-8") # 将utf8(此时utf8编码的字符要是unicode string格式)编码转换成unicode编码
# print(s2)


f = io.open("onePoem", "r", encoding="utf-8")
# # 文件读写格式：
#
# data = f.read() # 此时会把文件的所有内容都读到内存中
for i in f:
    print(i.strip())
# f.write("hello,world".encode("utf-8"))
# # f.read([number]) number : 表示从读取到的文件内容中拿number个数个字符，python中，一个中文和一个英文都是占一个字符
# print(data)
f.close()