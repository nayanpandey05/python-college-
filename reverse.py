arr=[1,2,3,4,5,6]
def array_reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=2
        right-=2
    return arr
print(array_reverse(arr))