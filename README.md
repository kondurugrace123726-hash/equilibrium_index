# equilibrium_index

## Equilibrium Index

Find an index where:
Sum of elements on the left == Sum on the right.
if no such index exist return -1

### Approach
- Calculate total sum
- Maintain running left sum
- Right sum = total - left - current

### Complexity
- Time: O(n)
- Space: O(1)
