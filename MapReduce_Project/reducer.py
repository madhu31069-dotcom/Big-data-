import os
from collections import defaultdict

os.makedirs("output", exist_ok=True)

result = defaultdict(int)

folder = "partitions"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        with open(os.path.join(folder, file), "r") as f:
            for line in f:
                key, value = line.strip().split(",")
                result[key] += int(value)

with open("output/final_output.txt", "w") as f:
    for key in sorted(result.keys()):
        f.write(f"{key} {result[key]}\n")

print("Reduction Completed!")
print("\nFinal Output:")

for key in sorted(result.keys()):
    print(f"{key} : {result[key]}")