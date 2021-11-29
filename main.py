def find3Numbers(Array, arr_size, sum):

    Array.sort()

    for i in range(0, arr_size - 2):

        left = i + 1

        right = arr_size - 1
        while left < right:

            if Array[i] + Array[left] + Array[right] == sum:
                print("Triplet is", Array[i],
                      ', ', Array[left], ', ', Array[right])
                return True

            elif Array[i] + Array[left] + Array[right] < sum:
                left += 1
            else:
                right -= 1

    return False


Array = list(range(1, 1000))
sum = 2500
arr_size = len(Array)

find3Numbers(Array, arr_size, sum)