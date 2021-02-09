'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeroes = []
    nonZeroes = []

    for i in arr:
        if i == 0:
            zeroes.append(i)
        else:
            nonZeroes.append(i)
    # return nonZeroes + zeroes
    
    # Improved method
    # initialize a left and right pointer
    # left is 0
    # right is last index in arr
    # left = 0
    # right = len(arr)
    # new_arr = []
    # # while left <= right:
    # while left < right:
    #     # if left points at a zero and right points at non-zero
    #     if arr[left] == 0 and arr[right-1] != 0:
    #         # swap left and right items in original arr
    #         new_arr.append(arr[right-1])
    #         # # increment left
    #         left += 1
    #         # # decrement right
    #         right -= 1
    #     # else
    #     else:
    #         new_arr.append(arr[left])
    #         # if left is non-zero:
    #         if arr[left] != 0:
    #             # increment left
    #             left += 1
    #         # if right is zero:
    #         if arr[right-1] == 0:
    #         #     # decrement right
    #             right -= 1
                
    # return new_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")