'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def check_sums(c_arr, c_val):
    for i in range(len(c_arr)):
        if c_val > c_arr[i]:
            c_arr.pop()
            c_arr.insert(i, c_val)
            break
    return c_arr

def lucky_winner(arr,k):
    max_arr = [0]*k
   
    # Row subarrays
    for i in range(len(arr)):
        # Since each row only has 3 elements, take middle as reference
        left_sum = 0; right_sum = 0;
        left_sum = arr[i][0] + arr[i][1]
        right_sum = arr[i][1] + arr[i][2]

        if left_sum > max_arr[-1]:
            max_arr = check_sums(max_arr,left_sum)
        if right_sum > max_arr[-1]:
            max_arr = check_sums(max_arr, right_sum)

        # Column-wise sums are harder....
        ## TODO: Currently this method does not account for overlaps.
        ## With the sample input, this method returns [99, 91, 8]
        ## But both 99 and 91 use the 100 elem, which is disallowed. 
        if i == len(arr)-1:
            pass
        else:
            for j in range(3):
                ind_sum = arr[i][j] + arr[i+1][j]
                if ind_sum > max_arr[-1]:
                    max_arr = check_sums(max_arr,ind_sum)

    return max_arr

if __name__ == '__main__':
    n, k = list(map(int,input().split()))

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(lucky_winner(arr,k))
