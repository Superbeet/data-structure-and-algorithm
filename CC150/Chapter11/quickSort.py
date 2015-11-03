def quickSort(arr, left, right):
	index = partition(arr, left, right)

	if left < index-1:
		quickSort(arr, left, index-1)

	if index < right:
		quickSort(arr, index, right)

def partition(arr, left, right):
	pivot = arr[(left+right)/2]

	while left<=right:

		while arr[left]<pivot:
			left += 1

		while arr[right]>pivot:
			right -= 1

		while left<=right:
			arr[left],arr[right] = arr[right],arr[left]
			left += 1
			right -= 1

	return left

if __name__ == "__main__":
	arr = [2,4,6,7,4,5,6,8,9,11,15,26,46,75]
	print arr
	quickSort(arr, 0, len(arr)-1)
	print arr