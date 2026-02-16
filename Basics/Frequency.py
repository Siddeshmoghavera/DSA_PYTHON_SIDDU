def most_frequent_frequency(arr):
    freq = {}

    # Count frequency of each element
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Find the maximum frequency
    max_freq = max(freq.values())

    return max_freq


# Input
arr = list(map(int, input("Enter elements: ").split()))

print("Frequency of Most Frequent Element:", most_frequent_frequency(arr))
