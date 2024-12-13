# Day 12: Garden Groups
https://adventofcode.com/2024/day/12

* [Part 1](./puzzle1.py) => `?????`
  - 1268400 -- too low
* [Part 2](./puzzle2.py) => `?????`


## Scratch Pad

```python
east = Direction("E")
if loc.look(east, self.__garden_map) == plant_type:
    easterly_loc = loc.copy()
    easterly_loc.move(east)
    if region.touches(easterly_loc):
        region.add_plot(loc)
        part_of_existing_region = True
```
