# -*- coding: utf-8 -*-
# author = "Louis"
from common.tools import ArrayGenerator, SortingTest
from merge_sort import MergeSort
import insertion_sort
import selection_sort

import copy
n = 100000
arr = ArrayGenerator.randomList(n)
arr2 = copy.deepcopy(arr)
arr3 = copy.deepcopy(arr)

MergeSort().sort(arr3)
selection_sort.main(arr2)
insertion_sort.main(arr)
print(SortingTest.isOrdered(arr3))
print(SortingTest.isOrdered(arr2))
print(SortingTest.isOrdered(arr))
print("Done!")