def slices(series, length):
    # checking series and length
    if length > len(series):
        raise ValueError("Series to short")

    if length < 1:
        raise ValueError("Slice legth must be positive")

    # creating the list
    slice = []
    # slicing
    for k in range(len(series) - length + 1):
        slice.append(series[k:k + length])

    return slice
