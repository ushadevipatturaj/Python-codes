def getOddOccurrence(arr):
    # Initialising an empty dictionary
    dictionary_count = {}
    for i in arr:
        if i in dictionary_count:
            dictionary_count[i] += 1
        dictionary_count.setdefault(i, 1)
    # getting the odd occurrences from the dictionary
    for value,count in dictionary_count.items():
        if count % 2 == 1:
            return value
print(getOddOccurrence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]))


def count_progress(times):
    previous_day = 0
    total_progress = 0
    for i,kms in enumerate(times):
        if i == 0:
            previous_day = kms
            continue
        else:
            if previous_day < kms :
                total_progress += 1
            previous_day = kms
    return total_progress

print(count_progress([3, 5, 7, 4, 4, 2]))


def find_distinct_element(numbers):
    # Initialising the default values
    unique_values = []
    for val in numbers:
        if val not in unique_values:
            unique_values.append(val)
        else:
            unique_values.remove(val)
    return unique_values

print(find_distinct_element([24,88,96,96,88,24,5,7,21,21]))