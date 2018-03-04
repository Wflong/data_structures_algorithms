import random
from single_link_list import SingleLinkList

'''插入排序，单链表的实现'''

def insert_sort_elem(l):
	'''通过元素的倒换实现排序'''
	cur =


def insert_sort_node(l):
	'''通过调整链接的方式实现排序'''
	pass


if __name__ == '__main__':
	l = SingleLinkList()
	for i in range(10):
		l.add(random.randrange(50))
	l.travel()
	print(l.length())