def split_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    mid = len(lines) // 2

    chunk1 = lines[:mid]
    chunk2 = lines[mid:]

    with open("chunk1.txt", "w") as f:
        f.writelines(chunk1)

    with open("chunk2.txt", "w") as f:
        f.writelines(chunk2)

    print("File splitted successfully!")

if __name__ == "__main__":
    split_file("input.txt")