demo_dict = {
    "aa": "AA",
    "bb": "BB",
    "cc": "CC"
}

# traverse dict key & value
for key in demo_dict.keys():
    print(key)

# traverse value
for val in demo_dict.values():
    print(val)

# traverse entry
for item in demo_dict.items():
    print(item[0] + ": " + item[1])

# traverse entry 2
for key, value in demo_dict.items():
    print(key + ": " + value)

# create number list by range. ps list would be: [)
for num in range(1, 10):
    print(num)

# range can also set step
for num in range(1, 10, 2):
    print(num)