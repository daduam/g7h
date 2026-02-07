def rotateLeft(d, arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        result[(i - d) % len(arr)] = arr[i]
    return result
