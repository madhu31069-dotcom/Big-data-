# MapReduce Engine using Python

A simple implementation of the MapReduce Engine in Python. This project demonstrates how a large input file is processed through the MapReduce workflow: Splitting, Mapping, Partitioning, Sorting, and Reducing.

## 📌 Project Overview

This project simulates the working of the MapReduce framework by processing text data and counting the occurrences of each category.

The workflow includes:

- Split the input file into smaller chunks.
- Convert each record into key-value pairs.
- Partition data among reducers using a hash function.
- Sort the partitioned data.
- Reduce the values to produce the final output.

---

## 📂 Project Structure

```
MapReduce_Project/
│
├── input.txt
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── master.py
├── chunk1.txt
├── chunk2.txt
├── map1.txt
├── map2.txt
├── partitions/
│   ├── partition0.txt
│   └── partition1.txt
├── output/
│   └── final_output.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Python 3
- File Handling
- Hash Function
- Dictionary
- Collections (defaultdict)

---

## 📥 Input

Example `input.txt`

```
Electronics
Accessories
Electronics
Clothing
Accessories
Electronics
Clothing
Furniture
Furniture
Electronics
```

---

## 🔄 Workflow

### 1. Splitter

Splits the input file into two chunks.

### 2. Mapper

Converts each record into a key-value pair.

Example:

```
Electronics
```

becomes

```
(Electronics,1)
```

### 3. Partitioner

Uses the following hash function to assign keys to reducers.

```
hash(key) % number_of_reducers
```

This ensures that the same key always goes to the same reducer.

### 4. Sorter

Sorts the partition files so identical keys are grouped together.

### 5. Reducer

Aggregates the values for each key and generates the final count.

---

## ▶️ How to Run

Run the files in the following order:

```bash
python splitter.py
python mapper.py
python partitioner.py
python sorter.py
python reducer.py
```

Or run the complete workflow using:

```bash
python master.py
```

---

## ✅ Sample Output

```
Accessories 2
Clothing 2
Electronics 4
Furniture 2
```

---

## 📚 Concepts Used

- MapReduce
- File Splitting
- Key-Value Pair
- Hash Partitioning
- Sorting
- Data Aggregation

---

## 🎯 Learning Outcome

Through this project, I learned:

- How the MapReduce framework works.
- Data processing using Python.
- File handling operations.
- Hash-based partitioning.
- Reducer aggregation logic.
- Building a mini MapReduce Engine from scratch.

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername
