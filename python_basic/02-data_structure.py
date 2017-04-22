# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/22
# @desc:

c = [1, 'abc', [1, 2]]
'''
c是一个列表，列表的第一个元素是整型1，第二个元素是字符串abc，第三个元素是列表[1, 2]
'''

'''
python有4个内建的数据结构，List（列表）、Tuple（元组）、Dictionary（字典）、Set（集合），统称为容器（container）
'''
# List mutable
a = [1, "2", 3]

# Tuple immutable
b = (1, "2", 3)
c = a[0]
d = b[0]
print c
print d
a[0] = 5
# b[0] = 5

b = a[:]  # 复制列表
print b
print 'List:%s, max:%s' % (a, max(a))

# ================ 列表方法 ================
a = [1, 2, 3]
b = [4, 5, 6]
# b = a[:]
print 'a列表：%s，b列表：%s' % (a, b)
print '比较a、b两个列表：%s' % cmp(a, b)  # 比较两个集合 相同返回0 不同返回-1
print 'a列表的长度:%d' % len(a)  # 返回列表的长度
print 'a列表中出现1的次数:%d' % a.count(1)
a.append(4)
print '向a列表追加元素：%s' % a
a.extend(b)
print '将列表b的内容追加到列表a的末尾:%s' % a
print '从列表a中找出第一个4的索引位置：%d' % a.index(4)
a.insert(2, 10)
print '向列表a的索引2位置插入值10：%s' % a
a.pop(2)
print "移除列表a的索引2的元素：%s" % a

