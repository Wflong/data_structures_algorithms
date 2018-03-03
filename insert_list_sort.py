
import random

'''插入排序，顺序表的实现'''


def insert_sort(l):
	count = len(l)
	for i in range(1, count):
		j = i - 1
		key = l[i]
		while j >= 0:
			if l[j] > key:
				l[j+1] = l[j]
				l[j] = key
			j -= 1
	return l


l = [x for x in map(lambda x:random.randrange(50), range(10))]
print('原始列表：', l)
insert_sort(l)
print('排序后的列表：', l)