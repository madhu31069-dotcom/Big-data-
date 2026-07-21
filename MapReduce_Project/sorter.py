import os

def sort_partition(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    lines.sort()

    with open(input_file, "w") as f:
        f.writelines(lines)

folder = "partitions"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        sort_partition(os.path.join(folder, file))

print("Sorting Completed!")