# Day 5: Cafeteria
https://adventofcode.com/2025/day/5

* Part 1: `inv run day05 1` => `789`
* Part 2: `inv run day05 2` => `?????`


## Scratch


### Tries
1. `269068590648661` -- too low
2. `302272241966923` -- too low
3. `308921066002250` -- too low

### Unfeasible solutions
```python
    # expand the range & add to unique list
    # entire number list is in memory :(
    # ---NO: runs out of memory (killed)---
    for iid in range(irng[0], irng[1]+1):
        fresh_iids[iid] = None
```

```python
    # Look at each iid in the range w/o keeping the entire
    # range in memory
    # ---NO: just too many numbers (billions) in each range (killed)---
    start = irng[0]
    end = irng[1]
    iid = start
    while iid >= start and iid <= end:
        fresh_iids[iid] = None
        iid += 1
```
