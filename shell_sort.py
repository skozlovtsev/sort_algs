def shell_sort(arr: list) -> list:
    step = len(arr)//2
    while step > 0:
        for i in range(0, len(arr), step):
            for j in range(i + step, len(arr), step):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        step = step // 2
    return arr

print(shell_sort([9, 4, 5, 8, 1, 7, 3, 2, 6]))
