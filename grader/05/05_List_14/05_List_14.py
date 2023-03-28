def peaks(x):
    # x: list of floats (or ints)
    # returns: list of indexes of peaks
    peaks_list = [i for i in range(1, len(x) - 1) if x[i - 1] < x[i] > x[i + 1]]
    return peaks_list


x = [int(e) for e in input().split()]
peaks_list = peaks(x)
print(len(peaks_list))