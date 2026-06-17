def longest_subarray_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
            
        current_window_size = right - left + 1
        if current_window_size > max_length:
            max_length = current_window_size
            
    return max_length

user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]
target_k = int(input("Enter maximum sum K: "))

result = longest_subarray_sum_k(nums, target_k)
print("Longest subarray length:", result)