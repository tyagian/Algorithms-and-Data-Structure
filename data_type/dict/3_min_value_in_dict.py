a_dictionary = {"a": 5, "b": 2, "c": 3}

# get key with min value
min_key = min(a_dictionary, key=a_dictionary.keys())

#min_key = min(a_dictionary.keys())
#min_key = min(a_dictionary.values())
print(min_key)
# print output => "a"