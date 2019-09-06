import random

def bubbleSort(lst):
	for i in reversed(range(1, len(lst))):
		for j in range(0, i):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]

	return lst

if __name__=="__main__":
	l = list()
	length = int(raw_input("ENTER # of NUMS: "))
	for i in range(0, length):
		l.append(random.randint(-100, 100))
	print("ORIGINAL LIST: {}".format(l))
	print("SORTED LIST: {}".format(bubbleSort(l)))
