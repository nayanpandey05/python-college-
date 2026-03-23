arr=[111,222,333]
def palindrome_array(arr):
    def is_pal(n):
        s=str(n)
        return s==s[::-1]
        return all(is_pal(x)for x in arr)
print(palindrome_array(arr))