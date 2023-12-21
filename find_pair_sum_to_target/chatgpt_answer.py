def find_pairs(arr, target):
    pairs = []
    num_dict = {}

    for num in arr:
        complement = target - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = True

    return pairs


