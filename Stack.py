
class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.size() == 0
	
	def push(self,item):
		return self.items.insert(0,item)
	
	def pop(self):
		return self.items.pop(0)
		
	def peek(self):
		return self.items[0]
		
	def size(self):
		return len(self.items)
		

