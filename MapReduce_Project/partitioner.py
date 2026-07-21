import os

NUM_REDUCERS = 2

os.makedirs("partitions", exist_ok=True)

# Empty partition files
for i in range(NUM_REDUCERS):
    open(f"partitions/partition{i}.txt", "w").close()

def partition(input_file):
    with open(input_file, "r") as f:
        for line in f:
            key, value = line.strip().split(",")

            reducer = hash(key) % NUM_REDUCERS

            with open(f"partitions/partition{reducer}.txt", "a") as p:
                p.write(f"{key},{value}\n")

partition("map1.txt")
partition("map2.txt")

print("Partitioning Completed!")