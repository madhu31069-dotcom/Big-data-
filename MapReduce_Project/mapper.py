def mapper(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    with open(output_file, "w") as f:
        for line in lines:
            key = line.strip()
            if key:
                f.write(f"{key},1\n")

    print(f"{output_file} created successfully!")

if __name__ == "__main__":
    mapper("chunk1.txt", "map1.txt")
    mapper("chunk2.txt", "map2.txt")