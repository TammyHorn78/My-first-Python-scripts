def isSorted(lst):
    # An empty list or a list with a single element is considered sorted.
    if len(lst) <= 1:
        return True
    
    # Loop through the list, comparing adjacent pairs.
    # The loop iterates up to the second-to-last element to compare each element with its successor.
    for i in range(len(lst) - 1):
        # If the current element is greater than the next element, the list is not sorted.
        if lst[i] > lst[i + 1]:
            return False
            
    # If the loop completes without finding any unsorted pair, the list is sorted.
    return True

def main():
    # The lists to use
    print(isSorted([]))               # Output: True
    print(isSorted([1]))              # Output: True
    print(isSorted([1, 2, 3, 4, 5]))  # Output: True
    print(isSorted([1, 3, 2, 4, 5]))  # Output: False
    print(isSorted([5, 4, 3, 2, 1]))  # Output: False
    print(isSorted([7, 3, 9, 2, 6]))  # Output: False
    print(isSorted([1, 3, 5, 7, 9]))  # Output: True


if __name__ == "__main__":
	main()
