example_dict = {"에이" : "A", "비" : "B", "씨" : "C"}

print("items : ", example_dict.items())
print(example_dict)


for key, i in example_dict.items():
    print("dict[{}] = {}".format(key, i))