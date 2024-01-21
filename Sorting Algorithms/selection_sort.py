# Selection Sort 

def selection_sort(a):
    print("Selection Sort Algorithm :-")
    print("")
    n=len(a)
    for i in range(0,n):
        print("")
        print("Round ",i+1," :- ")
        print(a)
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j 
        a[i],a[min_index]=a[min_index],a[i]
        print(a)
                
a=[9,8,7,6,5,4,3,2,1]
selection_sort(a)
print(a)

# Time Complexity :-
# Best Case :- O(n^2)
# Average Case :- O(n^2)
# Worst Case :- O(n^2)

# Space Complexity :- O(1)


# Example 

# [9,8,7,6,5,4,3,2,1]
# [1,8,7,6,5,4,3,2,9]
# [1,2,7,6,5,4,3,8,9]
# [1,2,3,6,5,4,7,8,9]
# [1,2,3,4,5,6,7,8,9]