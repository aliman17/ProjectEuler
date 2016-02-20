# HASHMAP

def map(key, modulo):
	return key % modulo

class HashTable(object):
	def __init__(self, size):
		self.size = size
		self.table = [None] * size
		self.counter = 0

	def insert(self,key, value):
		self.counter += 1
		if self.counter > 0.75*self.size:
			# Rehasshing
			pass
		modulo = self.size
		index = map(key, modulo)	
		if self.table[index]:
			self.table[index].append((key, value))
		else:
			self.table[index] = [(key, value)]


hash = HashTable(100)

hash.insert(5, 1000)
hash.insert(105, 2000)
hash.insert(99, 3000)
print(hash.table)		
