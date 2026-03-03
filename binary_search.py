lst = [1,2,3,4,5,6,7,8,9,10]
def binary_search(arr, target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
target=int(input("Enter the target number: "))
result=binary_search(lst,target)
if result != -1:
    print(f"Element found at index: {result}") 
else:
    print("Element not found in the list.")