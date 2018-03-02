# coding:utf-8
'''单链表 '''


class Node(object):
	'''结点类'''

	def __init__(self, elem):
		# elem用来保存数据
		self.elem = elem
		# 用来保存下一个节点
		self.next_= None


class SingleLinkList(object):
	'''单链表'''
	def __init__(self, node=None):
		'''初始化链表,'''
		node = Node(node)
		self.__head = node

	def is_empty(self):
		'''判断链表是否为空'''
		return self.__head.elem == None

	def length(self):
		'''返回这个链表的长度'''
		# 计数器用来记录元素的个数，也就是链表的长度
		count = 0
		if self.is_empty():
			return count
		# 创建一个游标来表示当前所指的节点
		cur = self.__head
		while cur != None:
			count += 1
			cur = cur.next_
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next_
		print("")

	def add(self, item):
		'''在链表头部添加元素,头插法'''
		node = Node(item)
		node.next_ = self.__head
		self.__head = node


	def append(self, item):
		'''在链表尾部添加元素,尾插法'''
		# 将item转换为Node类型的数据
		node = Node(item)
		# 判断当前链表是否为空
		if self.is_empty():
			self.__head = node
		# 不为空，找出next域是None的结点
		else:
			cur = self.__head
			while cur.next_ != None:
				cur = cur.next_
			cur.next_ = node

	def insert(self, position, item):
		'''在链表中的任意位置插入元素'''
		if position <= 0:
			self.add(item)
		elif position > self.length() - 1:
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (position - 1):
				count += 1
				pre = pre.next_
			# 当循环退出后，pre指向pos-1位置
			node = Node(item)
			node.next_ = pre.next_
			pre.next_ = node

	def remove(self, item):
		'''从链表中删除指定的元素'''
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				# 判断是否位头节点
				if cur == self.__head:
					# 是头结点
					self.__head = cur.next_
				else:
					pre.next_ = cur.next_
				break
			else:
				pre = cur
				cur = cur.next_

	def search(self, item):
		'''查找节点是否存在'''
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			cur = cur.next_
		return False


if __name__ == "__main__":
	sll = SingleLinkList(5)
	sll.travel()
	print("链表起始长度为：", sll.length())
	print("链表是否为空：", sll.is_empty())
	# 测试append()
	sll.append(1)
	sll.append(2)
	sll.append(3)
	sll.append(4)
	# print('追加之后的长度为：', sll.length())
	sll.travel()
	# 测试add()
	sll.add(5)
	sll.travel()
	# 测试insert
	sll.insert(3,9)
	sll.travel()
	print("链表现在长度为：", sll.length())
	print("链表现在是否为空：", sll.is_empty())
	# # 测试remove
	sll.remove(9)
	sll.travel()
	# 测试search
	print(sll.search(3))