# Linear Search

def linear_search(a,element):
    n=len(a)
    for i in range(0,n):
        if a[i]==element:
            return i 
    return -1
    
a=[9,8,7,6,5,4,3,2,1]
target_element=6
index=linear_search(a,target_element)
print("Linear Search Result:", index)

# Time Complexity :- 
# Best Case :- O(1) (when the target is at the beginning)
# Average Case :- O(n)
# Worst Case :- O(n)

# Space Complexity :- O(1) - constant space
