nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
result = list(map(lambda a, b: a + b if a > b else a - b, nums1, nums2))
print(result)
