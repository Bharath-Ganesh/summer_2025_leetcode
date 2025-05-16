# Intervals

## Key Concepts

- Interval representation (start, end points)
- Interval overlap detection
- Interval merging
- Interval scheduling
- Sweep line algorithm

## Problems and Solutions

### Easy

1. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
   - Key Learning: Basic interval overlap detection
   - Time Complexity: O(n log n)
   - Space Complexity: O(1)
   - Solution Approach: Sort by start time and check adjacent intervals

### Medium

1. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

   - Key Learning: Interval merging technique
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - Solution Approach: Sort and merge overlapping intervals

2. [Insert Interval](https://leetcode.com/problems/insert-interval/)

   - Key Learning: Handling interval insertions
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - Solution Approach: Three-part split approach

3. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
   - Key Learning: Interval scheduling
   - Time Complexity: O(n log n)
   - Space Complexity: O(1)
   - Solution Approach: Greedy selection based on end times

### Hard

1. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)
   - Key Learning: Complex interval manipulation
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - Solution Approach: Merge and find gaps

## Pattern Recognition

1. Sort First

   - Most interval problems require sorting by start or end times
   - Sorting simplifies overlap detection and merging

2. Sweep Line Technique

   - Useful for problems involving multiple intervals
   - Track events chronologically (start/end points)

3. Greedy Approach
   - Often optimal for interval scheduling problems
   - Usually involves sorting by end times

## Tips and Tricks

1. Always consider edge cases:

   - Empty interval list
   - Single interval
   - Completely overlapping intervals
   - No overlap at all

2. Choose the right sorting criteria:

   - Start time vs. End time
   - Impact on time complexity

3. Use helper functions:
   - Overlap detection
   - Merging logic
   - Interval comparison

## Common Mistakes to Avoid

1. Forgetting to sort intervals first
2. Incorrect overlap conditions
3. Not handling edge cases
4. Inefficient interval merging
5. Wrong sorting criteria selection

## Personal Notes

[Add your personal observations and learning experiences here]

## Resources

1. [Sweep Line Algorithm Explanation](https://www.geeksforgeeks.org/sweep-line-algorithm/)
2. [Interval Scheduling Algorithms](https://en.wikipedia.org/wiki/Interval_scheduling)
