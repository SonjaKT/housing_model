"""Implementation of list data type with associated sorting behaviors.

A list of numbers can be sorted easily using MergeSort, QuickSort, BubbleSort,
InsertionSort, or BucketSort. A list of any other data types can be sorted as 
well, as long as those data types support comparison operators (i.e. if a 
total preorder (a.k.a. non-strict weak order) exists on the data)."""

import random
import time
import sys

#sys.setrecursionlimit(20000)

class BasicList(object):

	def __init__(self, list_of_numbers = []):
		self._l = list_of_numbers
		self.methods = [self.merge_sort, self.bubble_sort, self.bucket_sort, self.insertion_sort, self.quick_sort_random]

	def get(self):
		return self._l

	def set(self, array):
		self._l = array

	def merge(self, list1, list2):
		"""Merge two sorted lists of numbers into a new sorted list containing 
		all elements of both original lists."""
		new_list = []
		while list1 and list2:
			if list1[0] < list2[0]:
				new_list.append(list1[0])
				list1.pop(0)
			else:
				new_list.append(list2[0])
				list2.pop(0)
		if list1:
			new_list.extend(list1)
		elif list2:
			new_list.extend(list2)
		return new_list

	def merge_sort(self, to_sort = None):
		if not to_sort:
			to_sort = self.get() #allows default parameter to be the list stored in self._l

		if len(to_sort) < 2: #base case: 0 or 1 elements in list
			return to_sort
		#if not len(to_sort) % 2: #length is even
		else:
			l1, l2 = to_sort[0:len(to_sort)/2], to_sort[len(to_sort)/2:]
			return self.merge(self.merge_sort(l1), self.merge_sort(l2))

	def swap(self, list_of_items, idx1, idx2):
		"""In-place swap list_of_items[idx1] with list_of_items[idx2]."""
		temp = list_of_items[idx1]
		list_of_items[idx1] = list_of_items[idx2]
		list_of_items[idx2] = temp

	def bubble_sort(self, to_sort = None):
		"""Iterate through list n times, comparing each successive pair of items. If any
		are out of order, swap them. In each round, the final item examined can be ignored in
		following rounds. O(n**2) time complexity in the worst case, but very fast to determine
		whether a list is already sorted -- i.e., O(n) in best case."""
		counter = 0

		if not to_sort:
			to_sort = self.get()

		flag = False
		while counter < len(to_sort):
			if flag: #if no swaps occurred in the last run, we can return
				break
			flag = True
			for idx in range(len(to_sort) - counter - 1):
				if to_sort[idx] > to_sort[idx+1]:
					self.swap(to_sort, idx, idx+1)
					flag = False
			counter += 1
			#print to_sort, counter
		return to_sort

	def insertion_sort(self, to_sort = None):
		"""Simple sorting algorithm to sort a list in-place with O(n**2) worst-case performance
		and Theta(n) best-case performance. Iterate through each item one at a time, and move it
		to the left while it is bigger than any item to its left."""
		if not to_sort:
			to_sort = self.get()

		for i in range(1,len(to_sort)):
			j = i
			while j>0 and to_sort[j-1]>to_sort[j]:
				self.swap(to_sort, j-1, j)
				j-=1

		return to_sort

	def bucket_sort(self, to_sort = None, max_val = None):
		"""Create an array of n 'buckets', each of size max_val / n. Iterate through the array to be
		sorted and place each value in the appropriate bucket. Then, put the buckets together into a new array
		and sort that with insertion sort. Requires values to be >= 0, and is most effective on evenly distributed data. 
		Insertion sort is used on the final array because its runtime is based on how far each element is from its 
		final destination, which is going to be small in this case as long as the data is well distributed across
		the buckets."""
		if not to_sort:
			to_sort = self.get()
		if not max_val:
			max_val = max(to_sort)
		
		bucket_size = max_val / float(len(to_sort)-1)
		bucket_list = [[] for i in range(len(to_sort))]
		#bucket_indices = [bucket_size * i for i in range(len(to_sort))]

		for item in to_sort:
			bucket_index = int(item / bucket_size)
			bucket_list[bucket_index].append(item)

		to_sort = []
		for bucket in bucket_list:
			to_sort.extend(bucket)

		return self.insertion_sort(to_sort)

	def quick_sort_random(self, to_sort = None):
		"""Choose a pivot element and recursively partition all elements of the array around
		the pivot. Many different possibilies exist for the pivot choice but random pivots
		have a good amortized runtime, beating out, e.g., always choosing the first element,
		especially when the list is already sorted."""
		if to_sort == None: #we cannot just do if not to_sort b/c we must be able to pass quick_sort an empty list
			to_sort = self.get()

		if len(to_sort) < 2: #base case
			return to_sort

		less, equal, greater = [], [], []
		pivot = random.choice(to_sort)
		#print pivot
		for item in to_sort:
			if item < pivot:
				less.append(item)
			elif item == pivot:
				equal.append(item)
			elif item > pivot:
				greater.append(item)
		return self.quick_sort_random(less) + equal + self.quick_sort_random(greater)

	def quick_sort_first(self, to_sort = None):
		"""Choose a pivot element and recursively partition all elements of the array around
		the pivot. For comparison with quick_sort_random, always choose the first element."""
		if to_sort == None: #we cannot just do if not to_sort b/c we must be able to pass quick_sort an empty list
			to_sort = self.get()

		if len(to_sort) < 2: #base case
			return to_sort

		less, equal, greater = [], [], []
		pivot = to_sort[0]
		#print pivot
		for item in to_sort:
			if item < pivot:
				less.append(item)
			elif item == pivot:
				equal.append(item)
			elif item > pivot:
				greater.append(item)
		return self.quick_sort_first(less) + equal + self.quick_sort_first(greater)

	def time(self, algorithm, array_length = 10000):
		#assess performance of algorithm on shuffled data
		items = [i for i in range(array_length)]
		random.shuffle(items)
		self.set(items)
		start = time.time()
		algorithm()
		shuffle_time = time.time() - start

		#assess performance of algorithm on already-sorted data
		items = [i for i in range(array_length)]
		self.set(items)
		start = time.time()
		algorithm()
		presort_time = time.time() - start

		return algorithm, shuffle_time, presort_time

	def multitime(self):
		array_lengths = [10**n for n in range(1,6)]
		time_dict = {}
		for alg in self.methods:
			time_dict[alg] = []
			for size in array_lengths:
				time_dict[alg].append(self.time(alg, size)[1:])
				print time_dict[alg]
		return time_dict

if __name__ == "__main__":
	# items = [i for i in range(1000)]
	# random.shuffle(items)
	# b = BasicList(items)
	# print b.quick_sort_first()
	b = BasicList()
	print b.multitime()


