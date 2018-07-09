#二分查找法
import random
import math
N = 10#数组元素个数
array = []
for i in range(N):
	temp = random.randint(0,99)
	#print(type(temp))
	#<class 'int'>
	array.append(temp)
#array 为随机数组
sorted_array = sorted(array)
print('array is ',sorted_array)
#sorted_array为排序好的数组
target = random.randint(0,99)#要查找的数
print('target is ',target)
def dichotomy(list):
	low = 0
	high = N-1
	key = math.ceil((low+high)/2)#向上取整
	for i in range(N):
		if target < list[0]:
			return None
			break
		if target > list[N-1]:
			return None
			break
		if target < list[key]:
			high = key - 1
		if target > list[key]:
			low = key + 1
		if target == list[key]:
			return key
			break
		if low == high:
			return None
			break
		key = math.ceil((low+high)/2)

print('result is ',dichotomy(sorted_array))
