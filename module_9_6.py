def subarrays(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(arr[i:j])
    return sorted(result, key=len)

def all_variants(text):
    for i in subarrays(text):
        yield i

a = all_variants("abc")
for i in a:
    print(i)
