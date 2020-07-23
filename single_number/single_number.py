'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import random
from time import time

def single_number(arr):
    '''
    set up a frequency counter that has once and twie
    for each num in arr
        if num in once 
            put into twice
        else
            put num into once
    
    return counter[once]
    '''
    # Your code here
    counter = {}

    for x in arr:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    
    for key, value in counter.items():
        if value == 1:
            return key
    
    return None

#O(1) space implementation

def single_number_n(arr):

    # Your code here
    singles = set()

    for x in arr:
        if x in singles:
            singles.remove(x)
        else:
            singles.add(x)
      
    return singles.pop()

def make_test_arr():
    arr = []

    for i in range(1000):
        arr.append(i)
        arr.append(i)

    random.shuffle(arr)
    rand_index = random.randint(0, len(arr))
    num = arr.pop(rand_index)
    return arr, num

if __name__ == '__main__':
    # Use the main function to test your implementation
    test_arr, num = make_test_arr()
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    # single_number(arr)
    start = time()
    print(f"The odd-number-out is {single_number(test_arr)}")
    end = time()
    print(f'\nRuntime: {end - start}')
    print(f"\nThe expected number is {num}")

