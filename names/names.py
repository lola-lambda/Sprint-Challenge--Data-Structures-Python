import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# 9s runtime:
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# 2s runtime with constrained space complexity:
# duplicates = [name for name in names_1 if name in names_2]

# 0.01s runtime:
names_1 = list(set(names_1))
names_2 = list(set(names_2))
merged_list = names_1 +names_2
encountered = {}
duplicates = []

for name in merged_list:
    if name in encountered:
        encountered[name] += 1
        duplicates.append(name)
    else:
        encountered[name] = 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

