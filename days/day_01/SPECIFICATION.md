# Day 01 - Advent of Code 2025

## Problem Statement

<!-- Paste the problem statement from adventofcode.com here -->

### Part One

Assuming a start position of 50, iterate through a set of instructions that adjusts this number left (decrease the position) or right (increase the position) and count the number of times throughout that the position stops at 0 after a move. 

We are working with a circular dial of positions 0-99, so moving left from 0 wraps around to 99, and moving right from 99 wraps around to 0.

### Part Two

As well as counting the number of times the position stops at 0, also track the number of times the position crosses over 0. Return the total number of crossings and stops at 0.

## Examples

Input:
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

## Part One Example Output:

Following these rotations would cause the dial to move as follows:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.

During this sequence, the dial stops at 0 three times.

## Part Two Example Output:


    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

Answer is 6

## Notes

<!-- Any additional notes, edge cases, or observations about the problem -->
