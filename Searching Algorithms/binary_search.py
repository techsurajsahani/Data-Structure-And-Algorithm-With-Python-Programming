# Binary Search 

def binary_search(a,target):
    
    low=0
    high=len(a)-1
    
    while low<=high:
        mid=(low+high)//2
        
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            low=mid+1 
        else:
            high=mid-1
    return -1 

a=[1,2,3,4,5,6,7,8,9]
target=7
result=binary_search(a,target)
print("Binary Search Result:", result)

# Time Complexity :- 
# Best Case :- O(1) (when the target is the middle element)
# Average Case :- O(log n)
# Worst Case :- O(log n)

# Space Complexity :- O(1) - constant space