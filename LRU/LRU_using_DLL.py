class ListNode():
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.prev = None
		self.head = None

class LRU_Cache():
	def __init__(self, capacity):
		self.size = capacity
		self.dict = {}
		self.head = ListNode(-1, -1)
		self.tail = ListNode(-1, -1)
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key):
		if key not in self.dict:
			return -1

		old_node = self.dict[key]
		self.remove(old_node)
		self.add(old_node)
		return old_node.val

	def put(self, key, value):
		if key in self.dict:
			old_node = self.dict.pop(key)
			self.remove(old_node)

		node = ListNode(key, value)
		self.add(node)

		if len(self.dict) > self.size:
			old_node = self.tail.prev
			self.remove(old_node)

	def remove(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

	def add(self, node):
		prev = self.tail.prev
		node.prev = prev
		node.next = self.tail
		self.tail.prev = node
		prev.next = node

def main():
	lru = LRU_Cache(1)
	lru.put(2, 1)
	print(lru.get(2))
	lru.put(3, 2)
	print(lru.get(2))
	print(lru.get(3))

if __name__ == "__main__":
	main()