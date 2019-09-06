import random

def max(x, y):
	if x > y:
		return x
	else:
		return y

def selectionSort(lst):
	for i in reversed(range(1, len(lst))):
		k = 0
		for j in range(1, i + 1):
			if lst[j] > lst[k]:
				k = j			
		lst[k], lst[i] = lst[i], lst[k]

	return lst

if __name__=="__main__":
	l = list()
	length = int(raw_input("ENTER LENGTH OF ARRAY: "))
	for i in range(0, length):
		l.append(random.randint(-1000, 1000))
	ret = selectionSort(l)
	print(ret)
