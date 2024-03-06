from collections import OrderedDict

class LRU_Cache():
	def __init__(self, capacity):
		self.size = capacity
		self.dict = OrderedDict()

	def get(self, key):
		if key in self.dict:
			self.dict.move_to_end(key)
			return self.dict[key]

		return -1

	def put(self, key, value):
		if key in self.dict:
			self.dict.move_to_end(key)
		
		self.dict[key] = value
		if self.size < len(self.dict):
			self.dict.popitem(last=False)

def main():
	lru = LRU_Cache(1)
	lru.put(2, 1)
	print(lru.get(2))
	lru.put(3, 2)
	print(lru.get(2))
	print(lru.get(3))

if __name__ == "__main__":
	main()