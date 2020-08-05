'''
Contiguous sum example visualized.

Feel free to use it :)

Would appreciate a plug at www.github.com/carrotsnotfound
'''

example_arr = [-2,1,-3,4,-1,2,1,-5,4]

best_sum = 0
current_sum = 0
counter=0

for i in range(len(example_arr)):
    
    print('')
    print('')
    print('Example Array:', example_arr)
    current_sum = current_sum + example_arr[i]
       
    print('Sub-array to sum', example_arr[counter:i+1])
    print('')
    print('Current Sum: ', current_sum)
    print('Best Sum (so far): ', best_sum)
    print('')
    
    if (current_sum < 0):
        print('Current sum is less than 0; re-initialize current sum to 0')
        current_sum = 0
        counter=i+1
        print('Next Step: create a new sub-array with next element')
    elif (best_sum < current_sum):
        print('Best sum so far is less than current sum; replace best sum value with current sum value')
        best_sum = current_sum
        print('Next step: Expand sub-array by 1 element')
    elif (current_sum < best_sum):
        print('Current sum is less than best sum so far; continue to next step')
        print('Next step: Expand sub-array by 1 element')

    print('-'*15)
    _ = input('Press Enter for Next Step...') 
    print('-'*15)


