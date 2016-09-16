import sys
import math
from yes_or_no import query_yes_no

myArray = [2,5,8,3,6,1,7]

def find_lowest_value_index(array, offset):
    lowestIndex = 0
    lowestValue = array[offset]

    for currentIndex, currentValue in enumerate(array[offset:]):
        if currentValue < lowestValue:
            lowestValue = currentValue
            lowestIndex = currentIndex

    return lowestIndex + offset

def array_swap(array, firstIndex, secondIndex):
    array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]
          
def selection_sort(unsortedArray):

    for index, value in enumerate(unsortedArray):
        lowestIndex = find_lowest_value_index(unsortedArray, index)
        array_swap(unsortedArray, index, lowestIndex)

    return unsortedArray

myArray = selection_sort(myArray)

print myArray




