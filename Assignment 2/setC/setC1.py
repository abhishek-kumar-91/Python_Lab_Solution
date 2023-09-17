
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) 
       
        if arr[mid] == target:
            return mid
  
        elif arr[mid] < target:
            left = mid + 1
       
        else:
            right = mid - 1

    return -1

sorted_list = [10, 20, 30, 40, 50, 60, 70]

target_element = 40

index = binary_search(sorted_list, target_element)
if index != -1:
    print(f"The element {target_element} is found at index {index}.")
else:
    print(f"The element {target_element} is not in the list.")