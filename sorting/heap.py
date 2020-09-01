"""
"""

class heap():
	def __init__(self):
		self.capacity = 10
		self.data = [0] * self.capacity
		self.slot = 0

	def heapify(self, index):
		left = 2*index+1
		right = 2*index+2
		
		parent_val = self.data[index]
		
		if left < self.slot and parent_val > self.data[left]:
			self.data[index], self.data[left] = self.data[left], self.data[index]

		if right < self.slot and parent_val > self.data[right]:
			self.data[index], self.data[right] = self.data[right], self.data[index]

	def push(self, item):
		index = self.slot
		self.slot += 1

		self.data[index] = item
		index = (index - 1) //2  
		while index >= 0:
			self.heapify(index)
			index  = (index - 1) // 2

	def pop():
		ans = self.data[0]
		
		index = slot-1
		self.data[0], self.data[index] = self.data[index], self.data[0]
		slot -=1	

		index = 0
		while index < self.slot:
			heapify(index)
			index = index  
		return ans

	def top():
		pass

	def sort():
		pass

	def print(self):
		print(self.data)

	def merge(*iterators):
		pass
		
from heapq import heapify, heappush, heappop, heapreplace, nsmallest, nlargest
def test_heap():
	H = []
	heappush(H, 2)
	heappush(H, 3)
	heappush(H, 8)
	heappush(H, 5)
	print(H)
	
def test_heap_class():
	H = heap()
	H.push(2)
	H.push(3)
	H.push(8)
	H.push(5)
		
	H.print()

test_heap()
test_heap_class()
