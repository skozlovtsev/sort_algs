def pivot(arr: list, p: int, f = 0):
    l = f
    while True:
        if arr[p] > arr[f]:
            l = l + 1
            if arr[f] < arr[l]:
                arr[f], arr[l] = arr[l], arr[f]
                f = f + 1
        f = f + 1
        if f == p:
            p = l + 1
            break
    return arr, p


def qs(arr: list, p: int) -> list:
    arr, p = pivot(arr, p)
    if p > 1:
        

def quicksort(arr: list) -> list:
    arr, p = pivot(arr, len(arr)-1)
    if p > 1:
        arr, p = pivot(arr, p)
        arr, p = pivot(arr, p)
        
