def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    freq = {}
    for sample in samples:
        freq[sample] = freq.get(sample, 0) + 1

    total = sum(freq.values())

    if total == 0:
        return []

    res = []
    for value in sorted(freq):
        probability = freq[value] / total
        res.append((value, probability))
    return res