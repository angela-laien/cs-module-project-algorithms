'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # zeroes = []
    # nonZeroes = []

    # for i in arr:
    #     if i == 0:
    #         zeroes.append(i)
    #     else:
    #         nonZeroes.append(i)
    # return nonZeroes + zeroes
    
    # Improved method
    # initialize a left and right pointer
    # left is 0
    # right is last index in arr
    i = 0
    left = arr[i]
    right = arr[len(arr)-1]
    new_arr = []
    # while left <= right:
    while left <= right:
        # if left points at a zero and right points at non-zero
        if left == 0 and right != 0:
            # swap left and right items in original arr
            new_arr.insert(right, left)
            # increment left
            i += 1
            # decrement right
            right -= 1
        # else
        else:
            # if left is non-zero:
            if left != 0:
                # increment left
                i += 1
            # if right is zero:
            if right == 0:
                # decrement right
                right -= 1
                
    return new_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")