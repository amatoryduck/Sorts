def max(x, y):
	if x > y:
		return x
	else:
		return y

def bubbleSort(lst):
	for i in reversed(range(1, len(lst))):
		for j in range(0, i):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]

	return lst

if __name__=="__main__":
	l = [4, 2,6 , 7, 1, -4, 1, -6, 1, 7, 1,4 , -7]
	print(bubbleSort(l))
