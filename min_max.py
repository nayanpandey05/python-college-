arr=[1,4,3,5,8,6]
def find_min_max(arr):
    if not arr:
        return[]
    min_val=max_val=arr[0]
    for num in arr[1:]:
        if num<min_val:
            min_val=num
        if num>max_val:
            max_val=num
    return [min_val,max_val]
print(find_min_max(arr))

