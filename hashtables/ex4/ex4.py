def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    new_dict = {}

    for num in a:
        new_dict[num] = num

        if num != 0 and - num in new_dict:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
