import random

def merge(lst1, lst2):
	i = 0
	j = 0
	ret = list()
	while i < len(lst1) or j < len(lst2):
		if i >= len(lst1) and j < len(lst2):
			ret.append(lst2[j])
			j = j + 1
		elif j >= len(lst2) and i < len(lst1):	
			ret.append(lst1[i])
			i = i + 1
		else:
			if lst1[i] <= lst2[j]:	
				ret.append(lst1[i])
				i = i + 1
			else:
				ret.append(lst2[j])
				j = j + 1
	return ret

def mergeSort(lst):
	if len(lst) <= 1:
		return lst
	else:
		n = len(lst)
		l = mergeSort(lst[0:(n/2)])
		r = mergeSort(lst[((n/2)):(n)])
		return(merge(l, r))

if __name__=="__main__":
	length = int(raw_input("ENTER # OF NUMS: "))
	lst = list()
	for i in range(0, length):
		lst.append(random.randint(-1000, 1000))
	print("ORIGINAL LIST: {}".format(lst))
	print("SORTED LIST: {}".format(mergeSort(lst)))
