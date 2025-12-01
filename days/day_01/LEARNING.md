# Day 01 - Learning Guide

## Problem Summary

This problem simulates a circular dial with 100 positions (0-99). Starting at position 50, we follow a series of rotation instructions (Left or Right) and need to track how many times the dial points at position 0.

- **Part One:** Count how many times we **stop** at position 0 after a move
- **Part Two:** Count how many times we **point at** position 0 (both stopping at 0 and passing through 0 during rotation)

## Key Concepts

- **Modular Arithmetic:** Using modulo operator to wrap around a circular structure
- **String Parsing:** Extracting direction and numeric values from text input
- **Simulation:** Step-by-step execution of instructions
- **Mathematical Counting:** Calculating how many times we pass through a position without simulating every single step
- **Edge Case Handling:** Special logic for moves starting from position 0

## Algorithm Explanation

### Part One

The solution is straightforward simulation:

1. **Parse the input** into a list of (direction, amount) tuples
2. **Start at position 50** on the circular dial
3. **For each instruction:**
   - Move left (subtract amount) or right (add amount)
   - Apply modulo 100 to wrap around the circular dial
   - If the new position is exactly 0, increment the counter
4. **Return the total count**

**Example trace:**
```
Start: 50
L68: 50 - 68 = -18 → -18 % 100 = 82
L30: 82 - 30 = 52
R48: 52 + 48 = 100 → 100 % 100 = 0 ✓ (count = 1)
L5:  0 - 5 = -5 → -5 % 100 = 95
R60: 95 + 60 = 155 → 155 % 100 = 55
L55: 55 - 55 = 0 ✓ (count = 2)
L1:  0 - 1 = -1 → -1 % 100 = 99
L99: 99 - 99 = 0 ✓ (count = 3)
R14: 0 + 14 = 14
L82: 14 - 82 = -68 → -68 % 100 = 32

Total: 3 stops at 0
```

### Part Two

Part Two requires counting not just stops but also passes through 0:

1. **Parse and initialize** as in Part One
2. **For each instruction:**
   - Store the old position
   - Calculate the new position with modulo
   - **Count how many times we point at 0 during this rotation:**
     - If starting at 0: Only count passes through 0 during the move (not the start)
     - If not starting at 0: Count all times we hit 0 during the rotation

**The key insight:** For large moves (> 100), the dial can pass through 0 multiple times!

**Counting formula for Left moves:**
- If `old_position == 0` and `amount >= 100`: count = `amount // 100`
- If `old_position != 0` and `amount >= old_position`: count = `1 + ((amount - old_position) // 100)`

**Counting formula for Right moves:**
- If `old_position == 0` and `amount >= 100`: count = `amount // 100`
- If `old_position != 0` and `total_distance >= 100`: count = `total_distance // 100`
  - where `total_distance = old_position + amount`

**Example trace:**
```
Start: 50
L68: 50 → 82 (crosses through 0 once) ✓ (count = 1)
L30: 82 → 52 (no crossing)
R48: 52 → 0 (stops at 0) ✓ (count = 2)
L5:  0 → 95 (starts at 0, no count)
R60: 95 → 55 (crosses through 0 once) ✓ (count = 3)
L55: 55 → 0 (stops at 0) ✓ (count = 4)
L1:  0 → 99 (starts at 0, no count)
L99: 99 → 0 (stops at 0) ✓ (count = 5)
R14: 0 → 14 (starts at 0, no count)
L82: 14 → 32 (crosses through 0 once) ✓ (count = 6)

Total: 6 times pointing at 0
```

## Code Walkthrough

### Parsing Input

```python
def parse_input(input_data: str) -> list:
    lines = input_data.strip().split('\n')
    instructions = []
    
    for line in lines:
        line = line.strip()
        if line:
            direction = line[0]      # Extract 'L' or 'R'
            amount = int(line[1:])   # Extract the number
            instructions.append((direction, amount))
    
    return instructions
```

This creates a clean data structure: `[('L', 68), ('L', 30), ('R', 48), ...]`

### Part One: Simple Modulo Logic

```python
position = 50
zero_count = 0

for direction, amount in instructions:
    if direction == 'L':
        position -= amount
    else:
        position += amount
    
    position = position % 100  # Wrap around the circular dial
    
    if position == 0:
        zero_count += 1
```

The modulo operator handles negative numbers correctly: `-18 % 100 = 82`

### Part Two: Mathematical Counting

Instead of simulating every step, we calculate mathematically:

```python
# Example: Moving right from position 50 by 150
# We pass through: 51, 52, ..., 99, 0, 1, ..., 99, 0, 1, ..., 50
# We hit 0 at position 100 and 200 (twice)

total_distance = 50 + 150  # = 200
times_at_zero = total_distance // 100  # = 2
```

This is much more efficient than looping 150 times!

**Edge case - starting at 0:**
```python
if old_position == 0:
    # Don't count the starting position
    # Only count times we hit 0 during the rotation
    if amount >= 100:
        times_at_zero = amount // 100
```

## Time and Space Complexity

### Part One
- **Time Complexity:** O(n) where n is the number of instructions
  - We process each instruction once with constant-time operations
- **Space Complexity:** O(n) to store the parsed instructions
  - Could be optimized to O(1) by parsing on-the-fly

### Part Two
- **Time Complexity:** O(n) where n is the number of instructions
  - Mathematical formulas avoid simulating individual steps
  - Each instruction is processed in O(1) time regardless of move amount
- **Space Complexity:** O(n) to store the parsed instructions

## What I Learned

### 1. Modular Arithmetic for Circular Structures
Python's modulo operator handles negative numbers elegantly:
- `-18 % 100 = 82` (wraps from 0 back to 99)
- This automatically handles circular wrapping without explicit conditionals

### 2. Mathematical Optimization
Instead of simulating every position in a large move, we can:
- Use integer division to count how many times we cross a boundary
- Example: Moving 1000 positions crosses 0 exactly 10 times

### 3. Edge Case Discovery
The trickiest edge case was handling moves **from** position 0:
- Initially, we might skip these moves entirely
- But we should still count passes through 0 during the rotation
- The key: don't count the starting position, only hits during the move

### 4. Test-Driven Development
Having multiple test cases helped catch edge cases:
- Empty input
- Single instructions
- Multiple passes through 0
- Starting at or near 0

## Related Topics

### Modular Arithmetic
- **Use cases:** Circular buffers, clock arithmetic, hashing
- **Python specifics:** `%` operator maintains sign convention (result has same sign as divisor)
- **Practice:** Rotating arrays, circular linked lists

### Simulation Problems
- **Pattern:** Step-by-step execution of instructions
- **Optimization:** Look for mathematical patterns to avoid simulating every step
- **Examples:** Robot movement problems, game state simulation

### Integer Division for Counting
- **Formula pattern:** `total // interval` counts complete intervals
- **Applications:** 
  - How many complete rotations?
  - How many times does X occur in range Y?
  - Counting multiples within a range

### Further Reading
- [Modular arithmetic (Wikipedia)](https://en.wikipedia.org/wiki/Modular_arithmetic)
- Python's `%` operator behavior with negative numbers
- Integer division and floor division in Python
- Circular data structures and algorithms
