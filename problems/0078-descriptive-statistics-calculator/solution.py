import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    arr = np.asarray(data, dtype=float)
    
    # mean
    n = len(arr)
    mean = sum(arr) / n

    # median
    nums = sorted(arr.tolist())
    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    
    # mode
    cnt = {}
    for num in nums:
        cnt[num] = cnt.get(num, 0) + 1
    
    max_freq = 0
    mode = 0
    for num, freq in cnt.items():
        if freq > max_freq:
            max_freq = freq
            mode = num
    
    # variance
    variance = 0
    for num in nums:
        variance += (num - mean) ** 2
    variance /= n
    
    # standard deviation
    standard_deviation = np.sqrt(variance)

    # quatile values
    def percentile(p):
        pos = (n - 1) * p / 100
        lower = int(pos)
        upper = min(lower + 1, n - 1)
        weight = pos - lower

        return nums[lower] + weight * (nums[upper] - nums[lower]) 

    q1 = percentile(25)
    q2 = percentile(50)
    q3 = percentile(75)

    # interquartile_range
    iqr = q3 - q1

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }
