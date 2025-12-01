# Sample 02 - Past Year Advent of Code Puzzle

## Problem Statement

### Part One

given a string of text, identify the parts of the text that match this pattern 
mul(x,y) where x and y are integers. For each match, calculate the product of x and y, and return the sum of all these products.

### Part Two

same as part one but ignore any instances of mul(x,y) following a "don't()" until the next occurrence of the word "do()", after which mul(x,y) instances should be counted again.

## Examples

part 1
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
produces 161 (2*4 + 5*5 + 11*8 + 8*5)

part 2
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
48 (2*4 + 8*5)

