def BinarySearch(arr, x):

	left = 0
	right = len(arr)-1

	while left<=right:

		mid = (left+right)/2

		if x<arr[mid]:
			right = left-1

		elif x>arr[mid]:
			left = right+1

		else:
			return mid

	return -1