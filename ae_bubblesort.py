"""
Overview:

Bubble sort is a O(n^2) sorting algorithm where it iterates 
through an array and checks if two elements in array are
greater than each other.

"""


def bubbleSort(array):
	# Create Flag to keep track of whether or not it's sorted
	sortedC = False

	while not sortedC:  # If the array is not sorted keep running while flag is false
		sortedC = True  # The Array is sorted if no swap occurs
		for i in range(1, len(array)):  # Iterate from 2nd ele to last
			prev = array[i-1]  # temp variables so simpler
			curr = array[i]
			if prev > curr:
				array[i-1], array[i] = array[i], array[i-1]  # Swap elements if condition
				sortedC = False	 # array isn't sorted so reset flag to restart loop
	return array
