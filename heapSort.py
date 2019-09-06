#!/usr/bin/env python

import random

def maxHeapify(lst):
	for i in reversed(range(0, int((len(lst)/2)))):
		sift(lst, i, len(lst))
	return lst

def sift(lst, index, n):
	while index < n:
		if (2 * index) + 1 < n and (2 * index) + 2 < n:
			l = (2 * index) + 1
			r = (2 * index) + 2
			if lst[l] >= lst[r]:
				if lst[l] > lst[index]:
					lst[l], lst[index] = lst[index], lst[l]
					index = l
				else:
					index = n
			elif lst[r] > lst[l]:
				if lst[r] > lst[index]:
					lst[r], lst[index] = lst[index], lst[r]
					index = r
				else:
					index = n
			else:
				index = n
		elif (2 * index) + 1 < n and (2 * index) + 2 >= n:
			l = (2 * index) + 1
			if lst[l] > lst[index]:
                                        lst[l], lst[index] = lst[index], lst[l]
                                        index = l
			else:
				index = n
		else:
			index = n
	return lst

def heapSort(lst):
	lst = maxHeapify(lst)
	for i in reversed(range(0, len(lst))):
		lst[0], lst[i] = lst[i], lst[0]
		lst = sift(lst, 0, i)
	return lst

if __name__=="__main__":
	length = int(raw_input("# of NUMS: "))
	nums = list()
	for i in range(0, length):
		nums.append(random.randint(-10000,10000))
	print("ORIGINAL LIST: {}".format(nums))
	print("HEAPED LIST: {}".format(maxHeapify(nums)))
	print("SORTED LIST: {}".format(heapSort(nums)))
