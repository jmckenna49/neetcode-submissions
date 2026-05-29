from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    output = defaultdict(int)
    for c in s:
        if c in output:
            output[c]+=1
        else:
            output[c]=1
    return output


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    counter_dict = defaultdict(list)
        
    for num_array in nums:
        counter_dict[num_array[0]].extend(num_array[1::])

    return counter_dict


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
