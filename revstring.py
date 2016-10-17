from Stack import Stack
def revstring(mystr):
	myStack = Stack()
	for ch in mystr:
		myStack.push(ch)
	revstr=''
	while not myStack.isEmpty():
		revstr = revstr + myStack.pop()
		
	return revstr
	
print (revstring('abcd'))