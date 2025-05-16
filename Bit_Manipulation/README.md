# Bit Manipulation

## Key Concepts

- Bitwise Operators (AND, OR, XOR, NOT)
- Bit Shifting (Left shift, Right shift)
- Bit Masking
- Power of Two Properties
- Binary Number System
- Two's Complement

## Problems and Solutions

### Easy

1. [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

   - Key Learning: Counting set bits
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Solution Approach: Brian Kernighan's algorithm

2. [Power of Two](https://leetcode.com/problems/power-of-two/)
   - Key Learning: Binary properties of powers of 2
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Solution Approach: Bit pattern recognition

### Medium

1. [Single Number](https://leetcode.com/problems/single-number/)

   - Key Learning: XOR properties
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Solution Approach: XOR all numbers

2. [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

   - Key Learning: Binary addition
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Solution Approach: Carry simulation with AND/XOR

3. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
   - Key Learning: Bit manipulation techniques
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Solution Approach: Divide and conquer

### Hard

1. [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
   - Key Learning: Complex bit manipulation
   - Time Complexity: O(2^(m\*n))
   - Space Complexity: O(2^(m\*n))
   - Solution Approach: State compression with BFS

## Pattern Recognition

1. Common Bit Operations

   - Setting bits
   - Clearing bits
   - Toggling bits
   - Checking bit status

2. Power of Two Properties

   - Binary representation
   - Manipulation techniques
   - Quick checks

3. XOR Properties
   - Self-cancellation
   - Commutative property
   - Finding unique elements

## Tips and Tricks

1. Bit Manipulation Shortcuts:

   - n & (n-1) removes rightmost set bit
   - n & (-n) isolates rightmost set bit
   - x ^ 0s = x
   - x ^ 1s = ~x
   - x ^ x = 0

2. Common Operations:

   - Left shift (<<) multiplies by 2
   - Right shift (>>) divides by 2
   - XOR swap without temp variable
   - Using masks for specific bits

3. Performance Optimization:
   - Avoid division/multiplication when possible
   - Use bit operations for power of 2
   - Leverage binary properties

## Common Mistakes to Avoid

1. Forgetting about negative numbers
2. Incorrect operator precedence
3. Not handling sign bit properly
4. Overflow/underflow in shifts
5. Assuming 32-bit integers

## Personal Notes

[Add your personal observations and learning experiences here]

## Resources

1. [Bit Manipulation Basics](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)
2. [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)
3. [Binary Arithmetic Tutorial](https://www.electronics-tutorials.ws/binary/bin_2.html)
