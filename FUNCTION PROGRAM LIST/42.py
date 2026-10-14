def extract_string(str_list1, l):
    return list(filter(lambda word: len(word) >= l, str_list1))

str_list1 = ["Python", "list", "exercises", "practice", "solution"]
l = 8
print(extract_string(str_list1, l))
