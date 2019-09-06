import random

def partition(lst, l, r):
	pivot = lst[r]
	i = l - 1
	for j in range(l, r):
		if lst[j] <= pivot:
			i = i + 1
			lst[i], lst[j] = lst[j], lst[i]
		
	lst[i + 1], lst[r] = lst[r], lst[i + 1]
	return (i + 1)

def quickSort(lst, l, r):
	if l < r:
		pivot = partition(lst, l, r)
		quickSort(lst, l, pivot - 1)
		quickSort(lst, pivot + 1, r)
	else:
		return lst		

if __name__=="__main__":
	l = list()
	length = int(raw_input("ENTER # of NUMS: "))
	for i in range(0, length):
		l.append(random.randint(-1000, 1000))
	print("ORIGINAL LIST: {}".format(l))
	quickSort(l, 0, len(l) - 1)
	print("SORTED LIST: {}".format(l))
