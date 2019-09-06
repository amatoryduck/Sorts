import random

def insertionSort(lst):
	for i in range(1, len(lst)):
		tmp = lst[i]
		j = i - 1
		while j >= 0 and tmp < lst[j]:
			lst[j + 1] = lst[j]
			j = j - 1
		lst[j + 1] = tmp

	return lst			

if __name__=="__main__":
	l = list()
	length = int(raw_input("ENTER # of NUMS: "))
	for i in range(0, length):
		l.append(random.randint(-100, 100))
	print("ORIGINAL LIST: {}".format(l))
	print("SORTED LIST: {}".format(insertionSort(l)))
