def max_sum_subarray(arr, k):
    n = len(arr)

    if n < k:
        return "Invalid Input: Window size K cannot be greater than the array length."
 
    current_window_sum = 0
    for i in range(k):
        current_window_sum += arr[i]

    max_sum = current_window_sum

    for i in range(k, n):

        current_window_sum += arr[i] - arr[i - k]

        if current_window_sum > max_sum:
            max_sum = current_window_sum
            
    return max_sum

user_array_string = input("Enter the array elements separated by spaces: ")

nums = [int(x) for x in user_array_string.split()]

k_size = int(input("Enter the window size (K): "))

result = max_sum_subarray(nums, k_size)
print(f"\nMaximum sum of a subarray of size {k_size} is: {result}")
