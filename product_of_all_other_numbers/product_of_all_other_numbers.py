'''
Input: a List of integers
Returns: a List of integers
'''
def multiply_num(myArr):
    if len(myArr) == 0:
        return 1
    else:
        product = 1
        for el in myArr:
            product = product * el
        return product

def product_of_all_other_numbers(arr):
    # Your code here
    multiple = []

    if len(arr) == 2:
        arr[0], arr[1] = arr[1], arr[0]
        return arr

    for i in range(0, len(arr)):
        if i == 0:
            right = arr[(i+1):]
            result = multiply_num(right)
            multiple.append(result)

        elif i == len(arr)-1:
            left = arr[:(i)]
            result = multiply_num(left)
            multiple.append(result)

        else:
            left = arr[:(i)]
            right = arr[(i+1):]
            rest = left + right
            result = multiply_num(rest)
            multiple.append(result)
    
    return multiple
    
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    arr = [9, 10]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
