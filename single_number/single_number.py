'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # for i in arr:
    #     if arr.count(i) == 1:
    #         return i

    # Improved method
        counts = {}
        # iterate through array
        for num in arr: # 0(n)
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        for k, v in counts.items():
            if v == 1:
                return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")