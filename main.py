def binary_search(arr, key, left, right):
    while left < right:
        center = (left + right) // 2

        if arr[center] == key:
            return center
        elif arr[center] < key:
            left = center + 1
        elif arr[center] > key:
            right = center - 1

    return left


def get_num(arr, sum):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        i = binary_search(arr, sum - arr[left] - arr[right], left + 1, right)
        curr_sum = arr[left] + arr[i] + arr[right]
        if curr_sum == sum and left != i:
            print("Yes", arr[left], arr[i], arr[right])
            return True
        elif curr_sum < sum:
            left += 1
        elif curr_sum > sum:
            right -= 1
    print("No")

    return False


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 6, 9, 3, 6, 24, 76, 34, 75, 24, 7, 66, 778, 2, 8, 3]
    search_sum = 75
    get_num(arr, search_sum)