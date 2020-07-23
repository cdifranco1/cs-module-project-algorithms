'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#first-pass solution
def sliding_window_max(nums, k):
    # Your code here
    left = 0
    right = k
    result = []
    
    while right < len(nums) + 1:
        curr_max = max(nums[left:right])
        result.append(curr_max)
        right += 1
        left += 1
    
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
