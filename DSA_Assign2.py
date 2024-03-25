import winsound
def merge_sort_with_sound(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  ######## Finding the middle of the array
        left_half = arr[:mid]  ######### Dividing the array elements into two halves
        right_half = arr[mid:]

        print("Splitting:", arr)  ######## the array before splitting

        merge_sort_with_sound(left_half)  ######### Sorting the first half
        merge_sort_with_sound(right_half)  ######## Sorting the second half

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            #### sound effect for swap
            winsound.Beep(1000, 100)  

        ##### Checking for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Merging:", arr)  #### array after merging

####### Function to take input from user for array elements
def take_input():
    input_str = input("Enter the numbers separated by commas: ")
    arr = [int(num) for num in input_str.split(",")]  ###### comma-separated numbers to integers
    return arr

#### Testing
arr = take_input()
print("Original Array:", arr)
merge_sort_with_sound(arr)
print("Sorted Array:", arr)
