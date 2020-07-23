'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
    # Your code here
    # start = 0
    # end = k
    # k_arr = []

    # for i in nums:
    #     window = nums[start:end]
    #     max_value = max(window)
    #     k_arr.append(max_value)

    #     if end < len(nums):
    #         start += 1
    #         end += 1
    #     else:
    #         break
    
    # return k_arr

def sliding_window_max(nums, k):
    output = []
    while 0 < len(nums) - (k-1):
        window = nums[0:k]
        output.append(max(window))
        nums.pop(0)
    return output

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
