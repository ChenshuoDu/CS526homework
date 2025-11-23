def radix_sort(arr):
    """
    LSD Radix Sort for non-negative integers.
    Returns a new sorted list.
    """
    if not arr:
        return []

    a = arr[:]

    max_num = max(a)
    exp = 1 

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]

        for number in a:
            digit = (number // exp) % 10
            buckets[digit].append(number)

        a = []
        for b in buckets:
            a.extend(b)
        exp *= 10 

    return a
