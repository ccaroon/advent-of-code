# Day 19: Linen Layout
https://adventofcode.com/2024/day/19

* [Part 1](./puzzle1.py) => `?????`
  * 328 -- too high
  * 292 -- nope
  * 252 -- too low
  * 130 -- too low
* [Part 2](./puzzle2.py) => `?????`

## Scratch Pad
        # DESIGN: bwurrg
        # look for bwu -> YES
        # -> ...rrg
        # look for wr -> NO
        # look for rb -> NO
        # look for gb -> NO
        # look for br -> NO
        # look for r -> YES
        # -> .....g
        # look for b -> NO
        # look for g -> YES
        # -> ......
        # -> design is empty
        # END -> MATCH

        # DESIGN -> brwrr
        # look for bwu -> NO
        # look for WR -> Yes
        # -> br..r
        # look for rb -> NO
        # look for gb -> NO
        # look for br -> YES
        # -> ....r
        # look for r -> YES
        # -> .....
        # END -> MATCH

        # DESIGN: bggr
        # look for bwu -> NO
        # look for wr -> NO
        # look for rb -> NO
        # look for gb -> NO
        # look for br -> NO
        # look for r -> YES
        # -> bgg.
        # look for b -> YES
        # -> .gg.
        # look for g -> YES (TWICE)
        # -> ....
        # END -> MATCH

        # DESIGN: ubwu
        # look for bwu -> YES
        # -> u...
        # look for wr,rb,gb,br,r,b  -> NO
        # look for g -> NO
        # -> not more towels
        # -> still colors in design
        # END -> NO MATCH
