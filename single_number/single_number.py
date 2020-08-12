'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    while len(arr) > 0:
        # select a number and remove it from the list
        number = arr.pop(0)

        # if the number is not in the list, we return the single number
        if number not in arr:
            return number

        # else we remove it by the value
        else:
            arr.remove(number)
    
        
        
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")