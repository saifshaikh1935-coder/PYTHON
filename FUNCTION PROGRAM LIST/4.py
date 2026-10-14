def unique_values(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print("Sample List:", sample_list)
print("Unique List:", unique_values(sample_list))
