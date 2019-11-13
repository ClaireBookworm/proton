class MyClass:
	# count : int?
	def __init__(self, count: int):
		self.count = count
	def __len__(self) -> int:
		return self.count

instance = MyClass(5)
print(len(instance))