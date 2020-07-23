'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    """
    set swap index at last index of arr
    increment backwards
        if num is zero:
            swap number with number at last index
    
    return array
    """
    swap_idx = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr[swap_idx], arr[i] = arr[i], arr[swap_idx]
            swap_idx -= 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")