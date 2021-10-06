
arr = [3, 1, 4, 1, 5, 9, 2, 6]
# arr = [1, 1, 2, 3, 4, 5, 6, 9]

print(arr)

# Traverse through 1 to len(arr) 
for i in range(1, len(arr)): 

    key = arr[i] 

    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key 
    
    print(arr)
  
# Driver code to test above 
print(arr)