from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, n in enumerate(nums):
        if n == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    # flags set to check if first and second indexes where 7 occur
    first_dist_flag = False
    second_dist_flag = False
    # dummy values to be filled with actual index values
    first_dist = 0
    second_dist = 0

    for i, n in enumerate(nums):
        if n == 7:
            if first_dist_flag == True:
                if second_dist_flag == False:
                    second_dist = i
                    second_dist_flag = True
            else:
                first_dist = i
                first_dist_flag = True
    total_dist = second_dist - first_dist
    return total_dist



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
