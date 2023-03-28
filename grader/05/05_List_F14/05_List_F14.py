def peaks(x):
    # x: list of floats (or ints)
    # returns: list of indexes of peaks
    peaks_list = [i for i in range(1, len(x) - 1) if x[i - 1] < x[i] > x[i + 1]]
    return peaks_list
exec(input()) # DON'T remove this line