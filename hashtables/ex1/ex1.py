def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1:
        return None
    elif limit == (weights[0] + weights[1]):
        return (1, 0)
    else:
        dictionary = {}

    for x in range(length):
        for y in range (1, length):
            sum = weights[x] + weights[y]
            dictionary[sum] = (x, y)
        if limit in dictionary:
            return dictionary[limit]

    return None
