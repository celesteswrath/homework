def binary_search(l, low, high, n):
	global counter
	if high >= low:
		middle = (high + low) // 2
		if l[middle] == n:
			return middle, low, high
		elif n < l[middle]:
			counter += 1
			return binary_search(l, low, middle-1, n)
		else:
			counter += 1
			return binary_search(l, middle+1, high, n)
	else:
		return -1

l = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91];
n = 70
counter = 1
result = binary_search(l, 0, len(l)-1, n)
print("index: ", result[0], " low: ", result[1], " high: ", result[2], " count: ", counter)