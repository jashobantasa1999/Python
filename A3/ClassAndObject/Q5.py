# 5. WAP to compute number of objects of a class has been created
# using data hiding technique of class?
class Solution:
	__privateCounter = 0

	def sum(self):
		self.__privateCounter += 1
		

count = Solution()
count.sum()
count.sum()
count.sum()
count.sum()

print(count._Solution__privateCounter)
