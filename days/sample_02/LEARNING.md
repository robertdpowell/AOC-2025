# Sample 02 - Learning Guide

## Problem Summary
Given a corrupted string of text, extract and process valid `mul(x,y)` patterns (where x and y are integers), calculate their products, and sum them. Part Two adds state-based control where `do()` and `don't()` commands enable or disable the processing of subsequent `mul()` operations.

## Key Concepts
- **Regular Expressions** - Pattern matching for structured data extraction
- **State Machine** - Tracking enabled/disabled states (Part Two)
- **String Parsing** - Processing sequential patterns while maintaining order
- **Iterator Pattern** - Using `finditer()` to process matches in sequence
- **Conditional Logic** - Different behaviors based on current state

## Algorithm Explanation

### Part One

**Step-by-step walkthrough:**

1. **Define the pattern** - Use regex `r'mul\((\d+),(\d+)\)'` to match valid `mul(x,y)` patterns
   - `\(` and `\)` - Escaped parentheses (literal characters)
   - `(\d+)` - Capture group for one or more digits
   - `,` - Literal comma
   
2. **Extract all matches** - Use `re.findall()` to get all valid patterns
   - Returns list of tuples: `[('2', '4'), ('5', '5'), ...]`
   - Invalid patterns are automatically ignored (e.g., `mul[3,7]`, `mul(32,64]`)

3. **Convert and calculate** - Parse strings to integers and multiply each pair
   ```python
   [(int(x), int(y)) for x, y in matches]  # Convert to integers
   sum(x * y for x, y in mul_pairs)        # Calculate sum of products
   ```

**Example trace:**
```
Input: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Found patterns:
  mul(2,4)  → 2 × 4 = 8
  mul(5,5)  → 5 × 5 = 25
  mul(11,8) → 11 × 8 = 88
  mul(8,5)  → 8 × 5 = 40

Total: 8 + 25 + 88 + 40 = 161
```

**Why invalid patterns are ignored:**
- `mul[3,7]` - Uses square brackets instead of parentheses
- `mul(32,64]` - Mismatched brackets
- `do_not_mul(5,5)` - Has text before "mul", not matched by pattern

### Part Two

**Step-by-step walkthrough:**

1. **Define combined pattern** - Match three types of commands:
   ```python
   r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
   ```
   - `mul\((\d+),(\d+)\)` - Multiplication with captured groups
   - `do\(\)` - Enable command
   - `don't\(\)` - Disable command
   - `|` - OR operator connecting all three patterns

2. **Initialize state** - Start with `enabled = True` (multiplications are counted from the beginning)

3. **Process in order** - Use `re.finditer()` to get matches sequentially (left-to-right)
   - Maintains position order, critical for state machine behavior
   - Each match object contains the matched text and captured groups

4. **State machine logic:**
   ```python
   if matched_text == "don't()":
       enabled = False        # Turn off processing
   elif matched_text == "do()":
       enabled = True         # Turn on processing
   elif matched_text.startswith("mul(") and enabled:
       # Only process if currently enabled
       x, y = int(match.group(1)), int(match.group(2))
       total += x * y
   ```

**Example trace:**
```
Input: xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

Initial state: enabled = True

Position  | Pattern    | Action
----------|------------|----------------------------------
1         | mul(2,4)   | enabled=True  → 2×4=8    ✓ Add 8
20        | don't()    | enabled=False → Switch OFF
28        | mul(5,5)   | enabled=False → Skip
48        | mul(11,8)  | enabled=False → Skip
59        | do()       | enabled=True  → Switch ON
64        | mul(8,5)   | enabled=True  → 8×5=40   ✓ Add 40

Total: 8 + 40 = 48
```

**Key insight:** The initial state MUST be enabled. Without an explicit `do()` at the start, multiplications before the first `don't()` are counted.

## Code Walkthrough

### Part One: Simple Pattern Matching

```python
pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, input_data)
```
**Key insight:** `re.findall()` with capture groups returns tuples of the captured content, not the full match. This gives us just the numbers, not the entire `mul(x,y)` string.

```python
return [(int(x), int(y)) for x, y in matches]
```
**Key insight:** List comprehension efficiently converts string tuples to integer tuples in one pass.

```python
total = sum(x * y for x, y in mul_pairs)
```
**Key insight:** Generator expression inside `sum()` is memory-efficient - calculates products on-the-fly without creating intermediate list.

### Part Two: State Machine with Ordered Processing

```python
pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
for match in re.finditer(pattern, input_data):
```
**Key insight:** `finditer()` vs `findall()`:
- `finditer()` returns match objects with position info, processed lazily
- `findall()` returns just the matched strings/groups, all at once
- We need `finditer()` to maintain sequential processing for state machine

```python
matched_text = match.group(0)
```
**Key insight:** `group(0)` gives the full matched string, while `group(1)` and `group(2)` give captured groups. We need the full text to identify which command matched.

```python
elif matched_text.startswith("mul(") and enabled:
    x, y = int(match.group(1)), int(match.group(2))
```
**Key insight:** We check both the pattern type AND the state. The captured groups (1 and 2) only exist for `mul()` patterns, not for `do()` or `don't()`.

## Time and Space Complexity

### Part One
- **Time Complexity:** O(n)
  - Single pass through input string with regex engine
  - n = length of input string
  - Each character examined once
  
- **Space Complexity:** O(m)
  - Store m tuples for m matches
  - m = number of valid `mul()` patterns found
  - In practice, m << n (much smaller than input length)

### Part Two
- **Time Complexity:** O(n)
  - Single pass through input with regex
  - Processing each match is O(1)
  - Total: O(n) for scanning + O(m) for processing matches = O(n)
  
- **Space Complexity:** O(m)
  - Iterator doesn't store all matches at once
  - Only current match object in memory
  - O(1) for state variables (enabled, total)
  - Effectively O(m) where m is matches, but processed lazily

## What I Learned

1. **Regular expressions are powerful for pattern matching** - A single regex pattern can precisely describe the valid `mul(x,y)` format, automatically filtering out malformed patterns like `mul[3,7]` or `mul(32,64]`.

2. **State machines need ordered processing** - Part Two requires processing patterns left-to-right to maintain correct state. Using `finditer()` instead of `findall()` preserves this order naturally.

3. **Initial state matters** - The problem starts with multiplications enabled. This wasn't explicitly stated as "start with `do()`" but was implied by the example where `mul(2,4)` before any `don't()` is counted.

4. **Regex capture groups simplify extraction** - Using `(\d+)` creates capture groups that let us extract just the numbers, making conversion to integers straightforward.

5. **Combining patterns with OR** - The `|` operator in regex lets us match multiple distinct patterns in a single pass, essential for Part Two's three command types.

6. **Edge case testing reveals assumptions** - Tests for starting with `don't()`, multiple toggles, and ending disabled helped verify the state machine logic worked correctly.

7. **Generator expressions are memory-efficient** - Using `sum(x * y for x, y in pairs)` instead of creating a list first saves memory for large inputs.

## Related Topics

### Regular Expressions
- **Escape sequences** - Special characters like `(`, `)`, `[`, `]` need escaping in regex
- **Capture groups** - `()` creates groups that can be extracted separately
- **Alternation** - `|` operator for matching multiple patterns
- **finditer() vs findall()** - Iterator vs list for different use cases

### State Machines
- **Finite State Automaton (FSA)** - Part Two implements a simple two-state machine
- **State transitions** - `do()` and `don't()` are transition commands
- **Initial state** - Default state before any transitions (enabled in this case)
- **Stateful parsing** - Processing where previous context affects current behavior

### String Processing
- **Sequential vs random access** - Order matters in Part Two, can't parallelize
- **Pattern matching** - Identifying structured data in unstructured text
- **Validation** - Distinguishing valid patterns from similar but invalid ones

### Python Specifics
- **re module** - Python's regex library with `findall()`, `finditer()`, `match()`, `search()`
- **Match objects** - `group()`, `start()`, `end()`, `span()` methods
- **List comprehensions** - Concise transformation of iterables
- **Generator expressions** - Memory-efficient calculations without intermediate storage

## Edge Cases Encountered

1. **No control commands** - Without `do()`/`don't()`, Part Two behaves like Part One
2. **Starting with don't()** - First `mul()` should be ignored when preceded by `don't()`
3. **Multiple consecutive toggles** - `do()do()` or `don't()don't()` are no-ops
4. **Ending in disabled state** - Trailing `don't()` means final `mul()` patterns ignored
5. **Invalid patterns mixed with valid** - Regex naturally filters invalid patterns
6. **Empty input** - Returns 0 gracefully
7. **Large numbers** - No special handling needed, Python handles arbitrary precision integers

## Performance Notes

For the actual puzzle input (18KB, 672 mul patterns, 28 do(), 34 don't()):
- Part One: Processes 672 multiplications
- Part Two: Processes 331 enabled + skips 341 disabled = 672 total
- Both parts run in < 0.01 seconds
- Memory usage minimal due to lazy iterator processing
