# Day 02 - Advent of Code 2025

## Problem Statement

<!-- Paste the problem statement from adventofcode.com here -->

### Part One

presented with a series of number ranges, we need to identify for each number range all numbers within that range (including the start and end numbers) that have a repeating sequence of numbers where that sequence repeats exactly twice in a row. For example, if the range is 10-30, we would look for numbers like 11 (one 1 repeated), 22 (one 2 repeated), 1212 (sequence of 12 repeated), 2323 (sequence of 23 repeated), etc.

examples of repeating sequences are 

55 (two 5s)
123123 (sequence of 123 repeated)
777 (three 7s)

then we should add up all of these numbers from all ranges and return the total.

### Part Two

same as part one but now the repeating pattern must appear at least twice in a row (i.e., four times total). For example, 12121212 (sequence of 12 repeated four times) or 9999 (four 9s).

## Examples


### Example Input

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

### Expected Output (Part One)


    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.

### Expected Output (Part Two)

4174379265

## Notes

<!-- Any additional notes, edge cases, or observations about the problem -->
