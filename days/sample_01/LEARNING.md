# Sample 01 - Learning Guide

## Problem Summary
Given two lists of numbers presented as pairs, we need to pair up the smallest numbers from each list, then the second smallest, and so on. For each pair, we calculate the absolute difference and sum all these differences to get a "total distance" between the two lists.

## Key Concepts
- **Input Parsing** - Splitting strings and converting to appropriate data types
- **Sorting** - Ordering lists to enable element-wise comparison
- **Zip Function** - Iterating over multiple lists in parallel
- **Absolute Value** - Calculating distance/difference regardless of sign
- **List Comprehension Alternative** - Could use sum/comprehension for more concise code

## Algorithm Explanation

### Part One

**Step-by-step walkthrough:**

1. **Parse the input** - Split each line into left and right numbers, storing them in separate lists
   - Line `"3   4"` → left: `3`, right: `4`
   - Build two lists: `[3, 4, 2, 1, 3, 3]` and `[4, 3, 5, 3, 9, 3]`

2. **Sort both lists independently**
   - Left sorted: `[1, 2, 3, 3, 3, 4]`
   - Right sorted: `[3, 3, 3, 4, 5, 9]`

3. **Pair up elements by position** and calculate differences
   - Position 0: `|1 - 3| = 2`
   - Position 1: `|2 - 3| = 1`
   - Position 2: `|3 - 3| = 0`
   - Position 3: `|3 - 4| = 1`
   - Position 4: `|3 - 5| = 2`
   - Position 5: `|4 - 9| = 5`

4. **Sum all differences**
   - Total: `2 + 1 + 0 + 1 + 2 + 5 = 11`

**Why sorting works:** By sorting both lists, we ensure that each number is paired with its closest counterpart in terms of magnitude, which gives us the minimum total distance when comparing ordered sequences.

### Part Two

**Step-by-step walkthrough:**

1. **Parse the input** - Same as Part One, split into two lists
   - Left list: `[3, 4, 2, 1, 3, 3]`
   - Right list: `[4, 3, 5, 3, 9, 3]`

2. **Count occurrences in the right list** using `Counter`
   - Creates a frequency map: `{3: 3, 4: 1, 5: 1, 9: 1}`
   - This allows O(1) lookup for each number's count

3. **Calculate similarity score** - For each number in the left list:
   - Number `3`: appears 3 times in right → `3 × 3 = 9`
   - Number `4`: appears 1 time in right → `4 × 1 = 4`
   - Number `2`: appears 0 times in right → `2 × 0 = 0`
   - Number `1`: appears 0 times in right → `1 × 0 = 0`
   - Number `3`: appears 3 times in right → `3 × 3 = 9`
   - Number `3`: appears 3 times in right → `3 × 3 = 9`

4. **Sum all products**
   - Total: `9 + 4 + 0 + 0 + 9 + 9 = 31`

**Key insight:** We process the left list in its original order, not sorted. Each occurrence of a number in the left list contributes to the score independently.

## Code Walkthrough

### Parsing Input
```python
lines = input_data.strip().split('\n')
left_list = []
right_list = []

for line in lines:
    left, right = line.split()  # Split on whitespace
    left_list.append(int(left))
    right_list.append(int(right))
```
**Key insight:** `split()` without arguments splits on any whitespace, handling multiple spaces between numbers automatically.

### Sorting and Calculating
```python
left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

total_distance = 0
for left, right in zip(left_sorted, right_sorted):
    total_distance += abs(left - right)
```
**Key insights:**
- `sorted()` returns a new sorted list without modifying the original
- `zip()` pairs elements from both lists by index
- `abs()` ensures we get positive distances regardless of which number is larger

### Alternative Implementation (More Pythonic)
```python
# Part One could be written as a one-liner:
total_distance = sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))

# Part Two using Counter:
from collections import Counter
right_counts = Counter(right_list)
similarity_score = sum(num * right_counts[num] for num in left_list)
```

## Time and Space Complexity

### Part One
- **Time Complexity:** O(n log n)
  - Parsing: O(n) - iterate through each line once
  - Sorting: O(n log n) - dominant operation, done twice
  - Calculating differences: O(n) - single pass through sorted lists
  - Overall: O(n log n) due to sorting

- **Space Complexity:** O(n)
  - Two lists to store parsed numbers: O(n)
  - Two sorted lists: O(n)
  - Overall: O(n) for storing the input data

### Part Two
- **Time Complexity:** O(n)
  - Parsing: O(n) - iterate through each line once
  - Building Counter: O(n) - iterate through right list once
  - Calculating similarity: O(n) - iterate through left list once
  - Overall: O(n) - linear time, more efficient than Part One!

- **Space Complexity:** O(n)
  - Two lists to store parsed numbers: O(n)
  - Counter dictionary: O(k) where k is unique numbers in right list, worst case O(n)
  - Overall: O(n)

## What I Learned

1. **Different problems require different approaches** - Part One needed sorting (O(n log n)), while Part Two used frequency counting (O(n)). Understanding the problem requirements helps choose the right data structure.

2. **Counter is powerful for frequency problems** - Python's `Counter` from collections module makes counting occurrences trivial and provides O(1) lookup time.

3. **Sorting isn't always necessary** - Part Two processes the left list in its original order. Each duplicate in the left list independently contributes to the similarity score.

4. **Test-Driven Development catches edge cases** - The tests revealed that Part Two treats each occurrence in the left list separately, not just unique values.

5. **Hash maps (dictionaries) optimize lookups** - Instead of counting occurrences for each left number every time (O(n²)), we build a frequency map once and look up in O(1).

## Related Topics

### Part One Related
- **Sorting Algorithms** - Understanding time complexity of different sorting approaches (Timsort in Python)
- **Greedy Algorithms** - Part One uses a greedy approach by always pairing smallest with smallest
- **Manhattan Distance** - The absolute difference calculation is similar to Manhattan distance in 1D
- **Hungarian Algorithm** - For more complex optimal pairing problems
- **Python's `itertools`** - The `zip()` function is part of Python's iteration tools for working with multiple sequences

### Part Two Related
- **Hash Tables / Dictionaries** - Understanding O(1) lookup time and how Counter is implemented
- **Frequency Analysis** - Counting occurrences is a common pattern in many algorithms
- **Python's `collections` module** - Counter, defaultdict, and other useful data structures
- **Similarity Metrics** - This similarity score is a weighted intersection between two lists
- **Multisets** - The problem treats lists as multisets where duplicates matter

## Edge Cases to Consider

- **Empty input** - What if there are no pairs?
- **Unequal list lengths** - What if lists have different numbers of elements? (`zip()` stops at the shortest)
- **Negative numbers** - The `abs()` function handles this correctly
- **Duplicate numbers** - Sorting handles duplicates naturally by maintaining relative order
